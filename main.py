from cliente import Cliente
import threading

class Covid:
    # funcao generica usada para validar variaveis do tipo char

    genero = ''
    resu_Teste = ''
    tp_Teste = ''
    vacina = ' ' 
    idade = 0
    op = 0
    cont_R = 0
    cont_PCR = 0
    cont_Pos = 0
    cont_NEG = 0
    cont_NV = 0
    idade_menor = 0
    idade_maior = 0
    indice = 0
    estrogonof = 0 
    nr_telemovel = 0 
    RAP = 1000
    PCR = 3500 
    PER = 100 
    vlr_pagar = 0
    vlr_total = 0 
    passou = True 

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

    # funcao que armazenas os dados no ficheiro

    def salvarDados(self, genero,  nr_telemovel,  resu_Teste,  tp_Teste,  vacina, vlr_pagar,  idade):
        print("SALVAR ")

    # funcao que mostra a percentagem dos casos negativos e positivos
    def visualizarPER(self, a,  b,  c):

        per_Pos, per_Neg
        per_Pos = a * c / (a + b) 
        per_Neg = b * c / (a + b) 
        print("A percentagem dos casos positivos e': %d%% ", per_Pos) 
        print("A percentagem dos casos negativos e': %d%% ", per_Neg) 
    

    # funcao que visualiza a quantidade de testes realizado de cada tupo
    def visualizarTeste(self, a,  b) :
        print("TOTAL DE TESTES: %d \n", a+b) 
        print("A quantidade de testes Rapidos realizados foi: %d ", a) 
        print("A quantidade de testes PCR realizados foi: %d ", b) 
    

    # funcao que visualiza o valor total obitido
    def visualizarTotal(self, vlr_total) :
        # DecimalFormat mt = new DecimalFormat("###,###,###.00 MTS\n") 
        print("O valor total recebido pela empresa e': %0.2f MTS \n", vlr_total) 
    

    # funcao que visualiza a quantidade de pessoas que precisam de Vacina
    def visualizarNaoVacinados(self, cont_NV)  :
        print("A quantidade de pessoas que precisam de Vacina: %d \n", cont_NV) 
    

    # funcao que visualiza a pessoa mais velha e mais nova contaminada
    def visualizaPessoas(self, indice,  estrogonof) :
        print(" a pessoa mais nova contamina tem %d anos \n", indice) 
        print(" a pessoa mais velha contamina tem %d anos \n", estrogonof) 

    # funcao que faz a leitura do ficheiro Dados.txt
    def gerarEstatisticas(self, type) :
        print("************************************ESTATISTICAS**************************************")  # titulo da tabela
         
        print("===================================FIM DA ESTATISTICAS================================\n") 
    
    

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
        if op == 1:
            print("Introduza o nome do cliente")
            nome = input()
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

            if tp_Teste == 'R':
                vlr_pagar = self.RAP 
                self.cont_R += 1 
            elif tp_Teste == 'P':
                vlr_pagar = self.PCR 
                self.cont_PCR += 1 

            #vlr_total += vlr_pagar 

            cliente = Cliente(nome=nome, genero=genero,nr_telemovel=nr_telemovel,result_Teste=result_Teste,tp_Teste=tp_Teste,vacina=vacina,vlr_pagar=vlr_pagar, idade=idade,)
            cliente.visualizarDados()
            cliente.salvar()

            self.switch_resu_Teste (result_Teste)
            self.switch_vacina(vacina)

            passou = False  

        elif op == 2:
            Cliente.visualizarTodosDados()
             
        elif op ==  3:
            self.gerarEstatisticas('t')  #ver estatistica do tipo testes feitos (f)
             
        elif op ==  4:
            self.gerarEstatisticas('p')  #ver estatistica do tipo percentagem feitos (p)
             
        elif op ==  5:
            self.gerarEstatisticas('e')  #ver valor arrecadado (o)
             
        elif op ==  6:
            if (passou == True):
                print("porfavor execute a primeira opcao\n") 
            else:
                self.visualizarNaoVacinados(self.cont_NV) 
             
        elif op ==  7:
            if (passou == True):
                print("porfavor execute a primeira opcao\n") 
            else:
                self.visualizaPessoas(self.indice, self.estrogonof) 
             
        elif op ==  8:
            self.visualizaDados() 

        elif op ==  9:
            print(" Ate a proxima :)\n") 


    def switch_resu_Teste (self, resu_Teste) :
        if resu_Teste ==  'P':
            self.cont_Pos += 1
            if (self.cont_Pos == 1):
                indice = self.idade 

            idade_maior = self.achar_Maior(indice, self.idade, self.cont_Pos) 
            idade_menor = self.achar_Menor(indice, self.idade, self.cont_Pos)  

        elif resu_Teste ==  'N':
            self.cont_NEG += 1

    def switch_vacina (self, vacina) :
        if vacina ==  'S':
            #here
            self.salvarDados(self.genero, self.nr_telemovel,self.resu_Teste, self.tp_Teste, vacina, self.vlr_pagar, self.idade) 
                
        elif vacina ==  'N':
            self.cont_NV += 1

    def main(self):
        print("|=============SISTEMA DE GESTAO COVID==============|\n") 

        '''  server = SocketServer() #object Server
        serverThread = threading.Thread(target=server.start(), args=[]) #add a sever Thread
        serverThread.daemon = True #as daemon
        serverThread.start() #start sever Thread'''
        
        self.menu()
if __name__ == '__main__':
    c = Covid()
    c.main()
