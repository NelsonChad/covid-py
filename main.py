from cliente import Cliente
import threading
from conexao import DB

class ClienteDAO:

    def salvaCliente(self, nome, email, genero,  nr_telemovel, result_Teste, tp_Teste, vacina, vlr_pagar, idade):
        connectDB = DB() # db object

        connect = connectDB.conecta()
        cursor = connect.cursor()

        comando = f'INSERT INTO clientes(nome, email, genero, telefone, idade, result_teste, tipo_teste, tipo_vacina, valor_pagar) VALUES("{nome}","{email}","{genero}","{nr_telemovel}","{idade}","{result_Teste}","{tp_Teste}","{vacina}","{vlr_pagar}")'
        cursor.execute(comando)
        connect.commit() # Manda para o BD

        connect.close()
        cursor.close()

    def consultarClientes(self):
        connectDB = DB() # db object

        connect = connectDB.conecta()
        cursor = connect.cursor()
        comando = 'SELECT * FROM clientes'
        cursor.execute(comando)

        resultado = cursor.fetchall() #LER DADOS
        connect.close()
        cursor.close()

        return resultado

class Cliente():

    def __init__(self, nome, email, genero,  nr_telemovel, result_Teste, tp_Teste, vacina, vlr_pagar, idade):
        self.nome = nome
        self.email = email
        self.genero = genero
        self.nr_telemovel = nr_telemovel
        self.result_Teste = result_Teste
        self.tp_Teste = tp_Teste
        self.vacina = vacina
        self.vlr_pagar = vlr_pagar
        self.idade = idade

        # Meto que visualiza a tabela
    def visualizarDados(self):
        print("***********************************************DADOS DO CLIENTE***********************************************")  #titulo da tabela
        print("______________________________________________________________________________________________________________") 
        print("| Nome Cliente | E-mail | Genero | Nr de Telemovel | Idade | Resultado | Tipo Teste | Vacina | Valor a pagar |") 
        print("______________________________________________________________________________________________________________")
        print("%18s|%20s|%8s|%15s|%10s|%6s|%9s|%8s|%12.2f MT|" % (self.nome, self.email, self.genero, self.nr_telemovel, self.idade , self.result_Teste , self.tp_Teste , self.vacina , float(self.vlr_pagar)))  #to see
        print("______________________________________________________________________________________________________________") 
        print("\n") 

    def salvar(self):
        dao = ClienteDAO()
        dao.salvaCliente(
            self.nome,
            self.email,
            self.genero,
            self.nr_telemovel,
            self.result_Teste,
            self.tp_Teste,
            self.vacina,
            self.vlr_pagar,
            self.idade
        )

    def visualizarTodosDados():
        dao = ClienteDAO()
        
        print("*****************************************************DADOS DOS CLIENTES*********************************************************")  #titulo da tabela
        print("________________________________________________________________________________________________________________________________") 
        print("| ID |   Nome Cliente   |       E-mail       | Genero | Nr de Telemovel | Idade | Resultado | Tipo Teste | Vacina | Valor Pago |") 
        print("________________________________________________________________________________________________________________________________")
        for cliente in dao.consultarClientes():
            print("|%4d|%18s|%20s|%8s|%15s|%10d|%6s|%9s|%8s|%12.2f MT|" % (int(cliente[0]) ,cliente[1] , cliente[4] , cliente[2] , cliente[3] , cliente[5] , cliente[6] ,cliente[7] ,cliente[8] , float(cliente[9])))
       
        print("________________________________________________________________________________________________________________________________") 
        print("\n") 


    def visualizarTeste():
        dao = ClienteDAO()

        results = dao.consultarClientes()
        totalTestes = 0
        qtdRapidos = 0
        qtdPCR = 0

        #print("ERSULT: ", results)

        totalTestes =len(results) # tamanho da lista
        for resultados in results:
            if(resultados[7] == 'R'):
                qtdRapidos += 1
            if(resultados[7] == 'P'):
                qtdPCR += 1
        print("************************************ESTATISTICAS**************************************")  # titulo da tabela
        print("TOTAL DE TESTES: ", totalTestes)
        print("A quantidade de testes Rapidos realizados foi: ", qtdRapidos)
        print("A quantidade de testes PCR realizados foi: ", qtdPCR)
        print("===================================FIM DA ESTATISTICAS================================\n")

    # funcao que mostra a percentagem dos casos negativos e positivos
    def visualizarPER():
        dao = ClienteDAO()
        results = dao.consultarClientes()
        per_Pos =0.0
        per_Neg = 0.0
        positivos =0
        negativos = 0

        for resultados in results:
            if(resultados[6] == 'P'):
                positivos += 1
            if(resultados[6] == 'N'):
                negativos += 1
 
        per_Pos = positivos * 100 / (positivos + negativos)
        per_Neg = negativos * 100 / (positivos + negativos)

        print("************************************ESTATISTICAS**************************************")  # titulo da tabela
        print("A percentagem dos casos positivos e': ", per_Pos, "%")
        print("A percentagem dos casos negativos e': ", per_Neg, "%")

    # funcao que mostra a percentagem dos casos negativos e positivos
    def visualizarTotal():
        dao = ClienteDAO()
        results = dao.consultarClientes()
        vlr_total = 0.0

        for resultados in results:
            vlr_total += float(resultados[9])
        
        print("************************************ESTATISTICAS**************************************")  # titulo da tabela
        print(f"O valor total recebido pela empresa e': {vlr_total} MTS ")

    # funcao que visualiza a quantidade de pessoas que precisam de Vacina
    def visualizarNaoVacinados()  :
        dao = ClienteDAO()
        results = dao.consultarClientes()
        cont_NV = 0

        for resultados in results:
            if(resultados[8] == 'N'):
                cont_NV += 1
        print("A quantidade de pessoas que precisam de Vacina: ", cont_NV) 

class Covid:
    # funcao generica usada para validar variaveis do tipo char
    passou = True 
    RAP = 1000
    PCR = 3500

    def validarchar(self, A,  B,  a,  b):
        e = ''
        while True:
            e = input()
            if (e != A and e != B and e != a and e != b):
                print("O tipo e invalido!Introduza novamente")
            else:
                return e

    # funcao generica para validar variaveis do tipo int
    def validarInt(self, a, b):
        n = 0
        while True:
            n = int(input())
            if (n < a or n > b):
                print("O valor introduzido e invalido! tente novamente\n")
            else:
                return n

    # funcao que ira fazer a validacao do numero de telemovel
    def validarnumero(self, a, b):
        c = 0
        while True:
            c = int(input())
            if (c < a or c > b):
                print("O Numero introduzido e invalido!\nVerifique se quantidade de digitos introduzida e corresponde a 9 algarismos e se contem os prefixos nacionais:\nTMCEL (82/83) \nVodacom (84/85) \nMovitel (86/87)\n")
            else:
                return c

    # funcao que tem a funcao de validar a idade
    def validaridade(self):
        n = 0
        while True:
            n = input()
            if (n < 0):
                print("Introduziu uma idade invalida! tente novamente\n")
            else:
                break
        return n
    
    

    # funcao que visualiza a pessoa mais velha e mais nova contaminada
    def visualizaPessoas(self, nova,  velha) :
        print(f" a pessoa mais nova contamina tem {nova} anos.", ) 
        print(f" a pessoa mais velha contamina tem {velha} anos.", ) 
        

    # funcao que acha a maior idade
    def achar_Maior(self, indice,  idade,  cont_Pos) :
        if (indice > idade):
            indice = idade 

        return indice 
    

    # funcao que acha a menor idade
    def achar_Menor(self, estrogonof,  idade,  cont_Pos) :
        if (estrogonof < idade):
            estrogonof = idade 
        return estrogonof 
    

    # funcao que visualiza dados do programador
    def visualizaDados(self) :
        print("Dado do Programador\n") 
    

        # funcao do Menu.
    def menu(self):
        while True:
            print("\n") 
            print("*************************MENU***********************\n") 

            print("1. Receber os dados do Paciente") 
            print("2. Visualizar todos os dados em forma de tabela") 
            print("3. Quantidade de Testes que foram feitos de cada Tipo") 
            print("4. Visualizar a percentagem dos casos Positivos e Negativos") 
            print("5. Valor total obtido pela empresa.") 
            print("6. Quantidade de pessoas que precisam de Vacina") 
            print("7 A a pessoa mais velha e mais nova contaminada") 
            print("8. Visualizar dados do programador") 
            print("9. Sair do Programa") 
            print("\n") 
            print("Por favor Escolha uma opcao") 

            op = self.validarInt(1, 9) 
            if op != 9:
                self.switch_cliente(op)
            else:
                break

    def switch_cliente(self, op):
        vlr_pagar = 0
        if op == 1:
            nome = input("Introduza o nome do cliente: ")
            email = input("Introduza o email: ")
            print("Introduza o tipo de teste que deseja realizar (R-Rapido P-PCR)\n") 
            tp_Teste = self.validarchar('R', 'P', 'r', 'p') 
            print("Introduza a idade do paciente(>0)\n") 
            idade = self.validarInt(0, 122) 
            print("Introduza o numero de telemovel do paciente ( Note que ele deve ter 9 digitos)\n") 
            nr_telemovel = self.validarnumero(820000000, 879999999) 
            print("Introduza o genero do paciente (M-masculino e F-femenino)\n") 
            genero = self.validarchar('M', 'F', 'm', 'f') 
            print("Introduza o resultado do teste do paciente (P-positivo ou N-negativo)\n") 
            result_Teste = self.validarchar('P', 'N', 'p', 'n') 
            print("informe o estado de vacinacao do paciente (S-sim ou N-nao)\n") 
            vacina = self.validarchar('S', 'N', 's', 'n') 

            if tp_Teste.upper() == 'R':
                vlr_pagar = self.RAP
            elif tp_Teste.upper() == 'P':
                vlr_pagar = self.PCR 

            cliente = Cliente(nome=nome,email= email, genero=genero.upper(),nr_telemovel=nr_telemovel,result_Teste=result_Teste.upper(),tp_Teste=tp_Teste.upper(),vacina=vacina.upper(),vlr_pagar=vlr_pagar, idade=idade,)
            cliente.visualizarDados()
            cliente.salvar()

        elif op == 2:
            Cliente.visualizarTodosDados()
             
        elif op ==  3:
            Cliente.visualizarTeste()
             
        elif op ==  4:
            Cliente.visualizarPER()  #ver estatistica do tipo percentagem feitos (p)
             
        elif op ==  5:
            Cliente.visualizarTotal()  #ver valor arrecadado (o)
             
        elif op ==  6:
            Cliente.visualizarNaoVacinados() 
             
        elif op ==  7:
            if (True):
                print("porfavor execute a primeira opcao\n") 
            else:
                self.visualizaPessoas(self.indice, self.estrogonof) 
             
        elif op ==  8:
            self.visualizaDados() 

        elif op ==  9:
            print(" Ate a proxima :)") 
            exit(0)


    def main(self):
        print("|=============SISTEMA DE GESTAO COVID==============|\n") 
        self.menu()

if __name__ == '__main__':
    c = Covid()
    c.main()
