import sqlite3

def inserir_professor(nome, materia, cpf):
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: este cpf ja esta cadastrado no sistema!")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

    finally:
        conexao.close()

# no código tem um erro de escrita no comando, e não tem um except para tratar esse erro. (COREÇÃO: trocar o INSERTO por INSERT e adicionar um except para tratar erro de digitação no código)        
                