import sqlite3

def cadastrar_escola_manual():
    conexao = None

    try:
        id_escola = int(input("Digite o ID para a nova escola: "))
        nome = input("Nome da escola: ")

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: Este ID de escola já está cadastrado!")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

    finally:
        if conexao:
            conexao.close()

# o código não tem um comando que trata quando tem id igual, e se colocar o mesmo id o programa fecha (COREÇÃO: adicionar o except para tratar erro se tiver id igual)