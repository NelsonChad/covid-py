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


