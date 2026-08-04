import sqlite3

def criar_banco():
    try:
        conexao = sqlite3.connect("hospital.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS hospitais(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm TEXT NOT NULL,
                id_hospital INTEGER,
                FOREIGN KEY(id_hospital) REFERENCES hospitais(id)
            )
        ''')

        conexao.commit()
        conexao.close()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)


def cadastrar_hospital():
    conexao = sqlite3.connect("hospital.db")
    cursor = conexao.cursor()

    nome = input("Digite o nome do hospital: ")
    cidade = input("Digite a cidade do hospital: ")

    comando = f"""
        INSERT INTO hospitais(nome, cidade)
        VALUES('{nome}', '{cidade}')
    """

    cursor.execute(comando)
    conexao.commit()
    conexao.close()

    print("Hospital cadastrado com sucesso!")


def cadastrar_medico():
    try:
        conexao = sqlite3.connect("hospital.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        nome = input("Digite o nome do médico: ")
        crm = input("Digite o CRM do médico: ")
        id_hospital = int(input("Digite o ID do hospital: "))

        cursor.execute(f"SELECT * FROM hospitais WHERE id = {id_hospital}")
        hospital = cursor.fetchone()

        if hospital is None:
            print("Erro! Hospital não encontrado.")
        else:
            comando = f"""
                INSERT INTO medicos(nome, crm, id_hospital)
                VALUES('{nome}', '{crm}', '{id_hospital}')
            """

            cursor.execute(comando)
            conexao.commit()
            print("Médico cadastrado com sucesso!")

        conexao.close()

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    except ValueError:
        print("Digite um ID válido!")


