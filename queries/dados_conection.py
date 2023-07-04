from enum import Enum


class DadosConexao(Enum):
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '123'
    DATABASE = 'data_vector'


class DataTableName(Enum):
    magnitude = "magnitude"
    coordenadas = "coordenadas"
