from conexao import DB

class ClienteDAO:

    def salvaCliente(self, nome, genero,  nr_telemovel, result_Teste, tp_Teste, vacina, vlr_pagar, idade):
        connectDB = DB() # db object

        connect = connectDB.conecta()
        cursor = connect.cursor()

        comando = f'INSERT INTO clientes(nome,genero,telefone,idade,result_teste,tipo_teste,tipo_vacina,valor_pagar) VALUES("{nome}","{genero}","{nr_telemovel}","{idade}","{result_Teste}","{tp_Teste}","{vacina}","{vlr_pagar}")'
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


