import pymysql


conexao = pymysql.connect(
    host='172.22.0.3',  # Endereço IP do container Docker
    port=3306,  # Porta mapeada para o contêiner
    user='root',
    password='1',
    database='data_vector'
)


cursor = conexao.cursor()


with open(f'../data_b_s/10co0206/bvals', 'r') as arquivo:

    linhas = arquivo.readlines()

    line_magnitude = [x.replace("\n", "") for x in linhas[0].split(" ") if x != '']


    # Iterar pelas linhas
    for magnitude in line_magnitude:

        # Extrair os valores de coordenadas x, y e z
        try:
            mag = float(magnitude)

        except:
            print(f"==={magnitude}")

        # Montar o comando SQL de inserção
        sql = "INSERT INTO magnitude (mag) VALUES (%s)"

        try:
            # Executar o comando SQL para inserir os valores
            cursor.execute(sql, mag)

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