import sqlite3

def criar():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()
        conexao.execute("PRAGMA foreign_keys = ON")


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS telecomunicacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_provedor TEXT NOT NULL,
                outorga_anatel TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS centrais_distribuicao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bairro_central TEXT NOT NULL,
                id_telecom INTEGER NOT NULL,
                FOREIGN KEY (id_telecom) REFERENCES telecomunicacoes(id)
            )
        """)
    
        conexao.commit()
        conexao.close()
    except sqlite3.Error as erro:
        print("Erro ao criar tabelas:", erro)
    except Exception as erro:
        print("Erro:", erro)

def cadastrar_telecom():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        nome_provedor = input("Digite o nome do provedor de internet: ")
        outorga_anatel = input("Digite o código da outorga da anatel: ")

        cursor.execute("""
            INSERT INTO telecomunicacoes (nome_provedor, outorga_anatel)
            VALUES (?, ?)
        """, (nome_provedor, outorga_anatel))

        conexao.commit()

        print("Provedor cadastrado com sucesso!")

        cursor.execute("SELECT * FROM telecomunicacoes")
        registros = cursor.fetchall()

        print(f"O banco possui: {registros}")
        conexao.close()

    except sqlite3.Error as erro:
        print("Erro ao cadastrar provedor:", erro)

def listar_telecom():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM telecomunicacoes")
        registros = cursor.fetchall()

        print(f"Registros encontrados: {registros}")

        if not registros:
            print("Nenhum provedor cadastrado!")
        else:
            for registro in registros:
                print(
                    f"ID: {registro[0]}, "
                    f"Provedor: {registro[1]}, "
                    f"Outorga ANATEL: {registro[2]}"
                )

        conexao.close()

    except sqlite3.Error as erro:
        print("Erro ao listar provedor:", erro)

def atualizar_telecom():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        id_busca_telecom = int(input("Digite o número do ID que deseja atualizar: "))
        cursor.execute(f'''SELECT * FROM telecomunicacoes WHERE ID = {id_busca_telecom}''')
        provedor_telecom = cursor.fetchone()

        if not provedor_telecom:
            print("Provedor não encontrado para realizar atualização!")
            conexao.close()
            return
        else:
            novo_nome_provedor = input("Digite o novo nome do provedor de internet: ")
            novo_outorga_anatel = input("Digite o novo código do outorga da anatel: ")

            comando = f''' UPDATE telecomunicacoes SET  nome_provedor = '{novo_nome_provedor}', outorga_anatel = '{novo_outorga_anatel}' WHERE id = {id_busca_telecom}'''

            cursor.execute(comando)
            print("Provedor atualizado!")
            conexao.commit()
            conexao.close()
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro ao atualizar provedor:", erro)
    except Exception as erro:
        print("Erro na atualização:", erro)

def excluir_telecom():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()
        listar_telecom()

        id_telecom_excluir = input("Digite o id do provedor que deseja excluir: ")
        cursor.execute(f''' DELETE FROM telecomunicacoes WHERE id = {id_telecom_excluir}''')

        print("Provedor excluido!")
        conexao.commit()
        conexao.close()
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.IntegrityError:
        print("Não é possível excluir este provedor porque existem centrais vinculadas a ele.")
    except sqlite3.Error as erro:
        print("Erro ao excluir provedor:", erro)
    except Exception as erro:
        print("Erro ao excluir:", erro)

def cadastrar_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db')  
        cursor = conexao.cursor()

        bairro_central = input("Digite o bairro da crentral: ")
        id_telecom = int(input("Digite o id o provedor: "))

        comando = f''' INSERT INTO centrais_distribuicao (bairro_central, id_telecom) VALUES ('{bairro_central}', '{id_telecom}')'''
        
        cursor.execute(comando)
        conexao.commit()
        print("Central cadastrada com sucesso!")
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados ao cadastrar central:", erro)
    except Exception as erro:
        print("Erro ao cadastrar central:", erro)
    conexao.close()

def listar_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db') 
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM centrais_distribuicao")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhuma central cadastrada!")  
        else:
            for registro in registros:
                print(f"ID: {registro[0]}, Bairro central: {registro[1]}, Id provedor: {registro[2]}") 
    except sqlite3.Error as erro:
        print("Erro no banco de dados ao listar central:", erro)
    except Exception as erro:
        print("Erro ao listar a central:", erro)

def atualizar_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        id_busca = int(input("Digite o id da central que deseja atualizar: "))
        cursor.execute(f''' SELECT * FROM centrais_distribuicao WHERE id = {id_busca}''')
        centrais = cursor.fetchone()

        if not centrais:
            print("Central não encontrada!")
            conexao.close()        
        else:
            novo_bairro = input("Digite o novo bairro da central: ")
            novo_id_provedor = int(input("Digite o novo id do provedor: "))

            comando = f''' UPDATE centrais_distribuicao SET bairro_central = '{novo_bairro}', id = '{novo_id_provedor}' WHERE id = {id_busca}'''
            
            print("Central alterada com sucesso!")
            cursor.execute(comando)
            conexao.commit()
            conexao.close()
           
    except ValueError:
        print("Os IDs devem ser números.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados ao atualizar central:", erro)
    except Exception as erro:
        print("Erro ao atualizar central:", erro)

def excluir_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        listar_central()
        id_busca_excluir = int(input("Digite o id da central que deseja excluir: "))

        cursor.execute(f''' DELETE FROM centrais_distribuicao WHERE id = {id_busca_excluir}''')
        conexao.commit()
        conexao.close()
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados ao excluir central:", erro)
    except Exception as erro:
        print("Erro ao excluir central:", erro) 

def menu():
    try:
        criar()
        while True:
            print("\n--- SISTEMA ISP ---")
            print("1- Cadastrar Provedor")
            print("2- Litar Provedor")
            print("3- Atualizar Provedor")
            print("4- Excluir Provedor")
            print("5- Cadastrar Central")
            print("6- Listar Central") 
            print("7- Atualizar Central")
            print("8- Excluir Central")
            print("0- Sair do Sistema")

            opcao = input("Escolha uma opção: ") 

            if opcao == "1":
                cadastrar_telecom()
            elif opcao == "2":
                listar_telecom()
            elif opcao == "3":
                atualizar_telecom()
            elif opcao == "4":
                excluir_telecom()
            elif opcao == "5":
                cadastrar_central()
            elif opcao == "6": 
                listar_central()
            elif opcao == "7":
                atualizar_central()
            elif opcao == "8":
                excluir_central()   
            elif opcao == "0":
                print("Saindo do Sistema...")
                break
            else:
                print("Opção invalida!") 

    except Exception as erro:
        print("Erro no menu:", erro)

menu()                


assert sqlite3.connect("provedor_internet.db").execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='telecomunicacoes'"
).fetchone() is not None

assert sqlite3.connect("provedor_internet.db").execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='centrais_distribuicao'"
).fetchone() is not None

assert sqlite3.connect("provedor_internet.db").execute(
    "SELECT COUNT(*) FROM telecomunicacoes"
).fetchone()[0] >= 0

assert sqlite3.connect("provedor_internet.db").execute(
    "SELECT COUNT(*) FROM centrais_distribuicao"
).fetchone()[0] >= 0

assert sqlite3.connect("provedor_internet.db").execute(
    "PRAGMA table_info(telecomunicacoes)"
).fetchall()[1][1] == "nome_provedor"

assert sqlite3.connect("provedor_internet.db").execute(
    "PRAGMA table_info(telecomunicacoes)"
).fetchall()[2][1] == "outorga_anatel"

assert sqlite3.connect("provedor_internet.db").execute(
    "PRAGMA table_info(centrais_distribuicao)"
).fetchall()[1][1] == "bairro_central"

assert sqlite3.connect("provedor_internet.db").execute(
    "PRAGMA table_info(centrais_distribuicao)"
).fetchall()[2][1] == "id_telecom"