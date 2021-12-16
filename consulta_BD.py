import mysql.connector

con = mysql.connector.connect(host='localhost', database='teste', user='root', password='123456')

consulta_sql = "select * from usuario"
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("numero total de registros é igual a {}".format(cursor.rowcount))

print('Mostrando os dados da tabela')
for linha in linhas:
    print('-----------------')
    print("nome: {}".format(linha[0])),
    print("idade:", linha[1]),
    print("cidade:", linha[2])
    print('-----------------')
    print('o {} nasceu na cidade de {} e tem {} anos'.format(linha[0], linha[2], linha[1]))

if con.is_connected():
    cursor.close()
    con.close()
    print('desconectado com sucesso')
