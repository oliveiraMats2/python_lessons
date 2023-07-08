import pymysql
import os

conexao = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='123',
    database='data_vector'
)


cursor = conexao.cursor()

ids_bvecs = [int(x) for x in os.listdir("../data_b_s/")]

for id_bvecs in ids_bvecs:
    with open(f'../data_b_s/{id_bvecs}/bvals', 'r') as arquivo:

        linhas = arquivo.readlines()

        line_magnitude = [x.replace("\n", "") for x in linhas[0].split(" ") if x != '']


        # Iterar pelas linhas
        for magnitude in line_magnitude:

            # Extrair os valores de coordenadas x, y e z
            try:
                id = int(id_bvecs)
                mag = float(magnitude)

            except:
                print(f"==={magnitude}")

            # Montar o comando SQL de inserção
            sql = "INSERT INTO magnitude (id, mag) VALUES (%s, %s)"

            try:
                # Executar o comando SQL para inserir os valores
                cursor.execute(sql, (id, mag))

                # Confirmar a transação
                conexao.commit()

                print(f"values ({mag}) in database")

            except Exception as e:
                # Reverter a transação em caso de erro
                conexao.rollback()
                print(f"Erro ao inserir os valores ({mag}): {str(e)}")

# Fechar o cursor e a conexão
cursor.close()
conexao.close()
