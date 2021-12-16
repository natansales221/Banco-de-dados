import mysql.connector

con = mysql.connector.connect(host="localhost", database='teste', user='root', password='123456')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conexão realizada com sucesso ao BD versão {}'.format(db_info))
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('conectado ao bd {}'.format(linha))

if con.is_connected():
    cursor.close()
    con.close()
    print('desconectado com sucesso')
