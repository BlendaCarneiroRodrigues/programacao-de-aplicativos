import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    tabelas_permitidas = ["alunos", "professores", "turmas"]

    if nome_tabela not in tabelas_permitidas:
        print("Tabela inválida!")
        return

    comando = f"SELECT * FROM {nome_tabela} WHERE id = ?"

    cursor.execute(comando, (id_registro,))

    print(cursor.fetchone())
    conexao.close()


# o caractere ? não é usado para nomes ou outras coisas ele é usado apenas para valores, (COREÇÃO: alterar o código para que não tenha erro, adicionar um if para mostrar que a tabela for invalida, criar uma variavel para por o comando)  