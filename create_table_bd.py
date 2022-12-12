import mysql.connector
from mysql.connector import Error
con = mysql.connector.connect(host='localhost', database='teste', user='root', password='123456')
if con.is_connected():
    print('Conectado')


choose = 0
try:
    while choose == 0 or choose > 3:
        choose = int(input('Pressione 1 para criar uma tabela ou 2 para apagar uma tabela: '))

        if choose == 1:
            table = str(input("digite o nome da tabela: "))
            create_table = 'create table ', table, ' (' \
                           'id_user int,' \
                           'nome varchar(30),' \
                           'idade int,' \
                           'telefone int ) '
            cursor = con.cursor()
            cursor.execute(create_table)
            print('tabela de nome ', table, ' com sucesso')

        elif choose == 2:
            table = str(input("digite o nome da tabela: "))
            drop_table = 'drop table ', table, ';'
            cursor = con.cursor()
            cursor.execute(drop_table)
            print('tabela de nome tal apagada com sucesso')

        elif choose == 3:
            break
except Error as e:
    print('houve um erro {}'.format(e))
# quando ler isso, localizar o código de consulta de banco de dados
# colocar o nome da tabela no "nome tal" escrito no código
# colocar while na programação (enquanto nao apertar a opção sair, continuará adicionando tabela)

if con.is_connected():
    cursor = con.cursor()
    con.close()
    cursor.close()
    print('Você foi desconectado com sucesso')
