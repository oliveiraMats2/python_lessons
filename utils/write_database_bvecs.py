import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='mateus',
    password='12345678',
    database='data_vector'
)


cursor = conexao.cursor()


with open(f'../data_b_s/100206/bvecs', 'r') as arquivo:

    linhas = arquivo.readlines()

    line_x = [x for x in linhas[0].split(" ") if x != '']
    line_y = [x for x in linhas[1].split(" ") if x != '']
    line_z = [x for x in linhas[2].split(" ") if x != '']

    # Iterar pelas linhas
    for x, y, z in zip(line_x, line_y, line_z):

        # Extrair os valores de coordenadas x, y e z
        try:
            x = float(x)
            y = float(y)
            z = float(z)
        except:
            print(f"{x}, {y}, {z}")

        # Montar o comando SQL de inserção
        sql = "INSERT INTO coordenadas (x, y, z) VALUES (%s, %s, %s)"

        try:
            # Executar o comando SQL para inserir os valores
            cursor.execute(sql, (x, y, z))

            # Confirmar a transação
            conexao.commit()

            print(f"values ({x}, {y}, {z}) in database")

        except Exception as e:
            # Reverter a transação em caso de erro
            conexao.rollback()
            print(f"Erro ao inserir os valores ({x}, {y}, {z}): {str(e)}")

# Fechar o cursor e a conexão
cursor.close()
conexao.close()