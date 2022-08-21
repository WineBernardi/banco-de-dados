from bd import nova_conexao

sql = 'SELECT * FROM contatos WHERE nome like %s'

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%', )# se coloca dois percentuais para que a letra ou sílaba
    # que for digitada seja encontrada em qualquer posição onde se encontra na palavra.
    #se colocar só no final se deseja encontrar a palavra que termina com aquela letra ou sílaba,
    #colocado na frente quer apenas as palavras que começa com aquela letra ou sílaba.

    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
