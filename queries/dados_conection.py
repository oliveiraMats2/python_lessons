from enum import Enum


class DadosConexao(Enum):
    HOST = 'localhost'
    USER = 'mateus'
    PASSWORD = '12345678'
    DATABASE = 'data_vector'


class DataTableName(Enum):
    magnitude = "magnitude"
    coordenadas = "coordenadas"
