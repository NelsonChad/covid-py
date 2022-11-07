import mariadb

class DB:
    def conecta(self):
        conexao = mariadb.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'covid_db',
        )
        return conexao