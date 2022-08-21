from bd import nova_conexao

sql = 'SELECT * FROM contatos WHERE nome like "%a%"' #lu% começa com lu e o resto e aleatório.

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)

        