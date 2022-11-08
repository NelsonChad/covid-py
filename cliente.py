from dao.clientesDAO import ClienteDAO


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
        print("*******************************DADOS DO CLIENTE*********************************")  #titulo da tabela
        print("_____________________________________________________________________________________") 
        print("| Nome Cliente | E-mail | Genero | Nr de Telemovel | Idade | Resultado | Tipo Teste | Vacina | Valor a pagar |") 
        print("_____________________________________________________________________________________")
        print("| ", self.nome," | ", self.email," | ", self.genero," | ", self.nr_telemovel," | ",self.idade ," | ", self.result_Teste ," | ", self.tp_Teste ," | ", self.vacina ," | ", self.vlr_pagar,"MT |")  #to see
        print("_____________________________________________________________________________________") 
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
        



        print("*******************************DADOS DOS CLIENTES*********************************")  #titulo da tabela
        print("_____________________________________________________________________________________") 
        print("| ID | Nome Cliente |  E-mail | Genero | Nr de Telemovel | Idade | Resultado | Tipo Teste | Vacina | Valor Pago |") 
        print("_____________________________________________________________________________________")
        for cliente in dao.consultarClientes():
            print("| ",cliente[0]," | ",cliente[1]," | ", cliente[2]," | ",cliente[3]," | ",cliente[4] ," | ",cliente[5]," | ",cliente[6] ," | ",cliente[7] ," | ",cliente[8] ," | ",cliente[9],"MT |")
            #print(cliente)
        print("_____________________________________________________________________________________") 
        print("\n") 