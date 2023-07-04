import pymysql
from queries.dados_conection import DadosConexao


class ConnectDatabase:
    @staticmethod
    def connect_my_database():#  -> Union[Connection[Cursor], Connection[Cursor]]:
        conexao = pymysql.connect(
            host=DadosConexao.HOST.value,
            port=3360,
            user=DadosConexao.USER.value,
            password=DadosConexao.PASSWORD.value,
            database=DadosConexao.DATABASE.value
        )
        return conexao

