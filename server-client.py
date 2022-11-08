import threading
import socket
import ast


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNao foi possivel conectar ao Servidor!\n')

    username = input('Nome do Cliente > ')
    print("Cliente: "+username+ " connectado!")

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=pedirDados, args=[client, username])

    thread1.start()
    thread2.start()

def menu():
    print("*************************MENU CLIENTE***********************\n") 
    print("1. Receber os dados Por Email") 
    print("2. Sair") 

def receiveMessages(client):
    while True:
        try:
            data = client.recv(2048).decode('utf-8')
            #print(data)

            if data == "False":
                print('DADOS DO UTILIZADOR NAO ENCONTRADOS NO SISTEMA')
                return
            else:
                #show data in table
                threadTable = threading.Thread(target=mostrarDados, args=[data])
                threadTable.start()
      
        except:
            print('Nao foi permanecer conectado ao server!\n')
            print('pressione Enter para continuar...')
            client.close()
            break

def pedirDados(client, username):
    while True:
        try:
            menu()
            op = int(input('\n'))
            if op == 1:
                client.send(f'{username}'.encode('utf-8'))
            elif op == 2:
                exit()
            else:
                print('OPCAO INVALIDA')
        except:
            return

def mostrarDados(data):
        cliente = ast.literal_eval(data)[0]
        #print('MY LIST: ', cliente)
        print("***********************************************SEUS DADOS**********************************************")  #titulo da tabela
        print("_______________________________________________________________________________________________________") 
        print("| ID | Nome Cliente |  E-mail | Genero | Nr de Telemovel | E-mail | Idade | Resultado | Tipo Teste | Vacina | Valor Pago |") 
        print("_______________________________________________________________________________________________________")
        
        print("| ",cliente[0]," | ",cliente[1]," | ", cliente[2]," | ",cliente[3]," | ",cliente[4] ," | ",cliente[5]," | ",cliente[6] ," | ",cliente[7] ," | ",cliente[8]," | ",cliente[9]," | ",cliente[10],"MT |")
            #print(cliente)
        print("_______________________________________________________________________________________________________") 
        print("\n") 
    
        menu()
main()

