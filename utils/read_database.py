from queries.open_connect_database import ConnectDatabase
from queries.dados_conection import DataTableName
import pymysql

if __name__ == "__main__":
    data = {
        "id": [],
        "mag": [],
        "x": [],
        "y": [],
        "z": []
    }
    connect = ConnectDatabase.connect_my_database()

    cursor = connect.cursor(pymysql.cursors.DictCursor)

    try:
        consulta_sql = f"SELECT * FROM {DataTableName.magnitude.value}"
        cursor.execute(consulta_sql)

        list_dict_data_magnitudes = cursor.fetchall()

        # Exibir os resultados
        for data_magnitude in list_dict_data_magnitudes:
            data["mag"].append(data_magnitude["mag"])

        consulta_sql = f"SELECT * FROM {DataTableName.coordenadas.value}"
        cursor.execute(consulta_sql)

        list_dict_data_coordinates = cursor.fetchall()

        for coordinate in list_dict_data_coordinates:
            data["x"].append(coordinate["x"])
            data["y"].append(coordinate["y"])
            data["z"].append(coordinate["z"])

        list_dict_data_magnitudes = cursor.fetchall()

    except Exception as e:
        print(f"Error in consult {str(e)}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        connect.close()

    print(data.keys())
