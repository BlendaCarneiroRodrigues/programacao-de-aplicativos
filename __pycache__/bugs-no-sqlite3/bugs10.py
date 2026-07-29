import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola))

    conexao.commit()
    conexao.close()

# o id_escola está sendo colocado de forma errada no cursor.execute. (COREÇÃO: colocar i id_escola entre ())    