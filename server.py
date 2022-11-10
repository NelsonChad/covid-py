import threading
import socket

from email_server import EmailServer
from conexao import DB

class ServerDAO:
    def consultarDados(self, nome):
        print('NA CONSULTA: ', nome)
        connectDB = DB() # db object

        connect = connectDB.conecta()
        cursor = connect.cursor()
        comando = f'SELECT * FROM clientes Where nome = "{nome}"'
        cursor.execute(comando)

        resultado = cursor.fetchall() #LER DADOS
        connect.close()
        cursor.close()

        return resultado

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
        print('Servidor Escutando...\n')

    except:
        return print('ERRO ao inicair servidor!\n')
    
    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    serverDAO = ServerDAO()
    while True:
        try:
            username = client.recv(2048)
            name = username.decode('utf-8')
            resp = serverDAO.consultarDados(name)
            msg =""
            
            if resp == []:
                print("DADOS DO UTILIZADOR NAO ENCONTRADOS")
                msg = "False"
            else:
                print("RESPOST : ",resp)

                #send data
                msg = resp
                broadcast(msg, client)
                #sendEmail(to_email=resp[4], subject="RESULTADOS",body=resp, client=client) #send Email

        except:
            deleteClient(client)
            break
        
def sendEmail(to_email,subject, body, client):
    message = f" Acaro Cliente {body[2]}, o teu resultado e': {body[7]}"
    try:
        print(message)
        client.send(str(message).encode())

        email = EmailServer(to_email=to_email, subject=subject,body=message) # send the email
        email.sendMail()
    except:
        deleteClient(client)

def broadcast(msg, client):
    try:
        client.send(str(msg).encode())
    except:
        deleteClient(client)

def deleteClient(client):
    clients.remove(client)

main()