import pymysql
from dados_conection import DadosConexao


class ConnectDatabase:
    @staticmethod
    def connect_my_database():
        conexao = pymysql.connect(
            host=DadosConexao.HOST.value,
            user=DadosConexao.USER.value,
            password=DadosConexao.password.value,
            database=DadosConexao.database.value
        )
        return conexao
