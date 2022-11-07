import threading
import socket

from dao.serverDao import ServerDAO
from email_server import EmailServer

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

'''def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break'''

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
                print("RESPORTA: ",resp)
                email = EmailServer(to_email=resp[4], subject="Resultados",body=resp) # send the email
                email.sendMail()

                #msg = f"DADOS: {name} {resp}"
                msg = resp


            broadcast(msg, client)
        except:
            deleteClient(client)
            break
    

def broadcast2(msg, client):
    for clientItem in clients:
        if clientItem == client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def broadcast(msg, client):
    try:
        client.send(str(msg).encode())
    except:
        deleteClient(client)

def deleteClient(client):
    clients.remove(client)

main()
