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
        outorga_anatel = input("Digite o código do outorga da anatel: ")

        comando_inserir = f''' INSERT INTO telecomunicacoes (nome_provedor, outorga_anatel)
                                VALUES ('{nome_provedor}', '{outorga_anatel}')'''
        
        cursor.execute(comando_inserir)
        conexao.commit
        print("Telecomunicações cadastrada")
    except sqlite3.Error as t:
        print(f"Erro ao cadastrar telecomunicações: {t}")
    finally:
        conexao.close()

def listar_telecom():
    try: 
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM telecomunicacoes")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum provedor cadastrado!")
        else:
            for registro in registros:
                print(f"ID: {registros[0]}, Provedor: {registros[1]}, Outorga ANATEL: {registros[2]}") 

    except sqlite3.Error as erro:
        print("Erro ao fazer listagem:", erro)
    except Exception as erro:
        print("Erro na listagem:", erro)

def atualizar_telecom():
    try:
        conexao = sqlite3.connect('provador_internet.db')
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

            comando = f''' UPDATE telecominicacoes SET  nome_provedor = '{novo_nome_provedor}', outorga_anatel = '{novo_outorga_anatel}' WHERE id = {id_busca_telecom}'''

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

        comando = f''' INSERT INTO centrais_distribuicao (bairro_central, id) VALUES ('{bairro_central}', '{id_telecom}')'''
        
        cursor.execute(comando)
        conexao.commit()
        print("Central cadastrada com sucesso!")
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    except Exception as erro:
        print("Erro:", erro)
    conexao.close()

def listar_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db') 
        cursor = conexao.cursor()

        cursor.execute("SELCT * FROM central_distribuicao")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhuma central cadastrada!")  
        else:
            for registro in registros:
                print(f"ID: {registro[0]}, Bairro central: {registro[1]}, Id provedor: {registro[2]}, Provedor: {registro[3]}") 
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    except Exception as erro:
        print("Erro:", erro)

def atualizar_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        id_busca = int(input("Digite da central que deseja atualizar: "))
        cursor.execute(f''' SELECT * FROM central_distribuicao WHERE id = {id_busca}''')
        centrais = cursor.fetchone()

        if not centrais:
            print("Central não encontrada!")
            conexao.close()        
        else:
            novo_bairro = input("Digite o novo bairro da central: ")
            novo_id_provedor = int(input("Digite o novo id do provedor: "))

            comando = f''' UPDATE central_distribuicao SET bairro_central = '{novo_bairro}', id = '{novo_id_provedor}' WHERE id = {id_busca}'''

            cursor.execute(comando)
            conexao.commit()
            conexao.close()
            conexao.close()
    except ValueError:
        print("Os IDs devem ser números.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    except Exception as erro:
        print("Erro:", erro)

def excluir_central():
    try:
        conexao = sqlite3.connect('provedor_internet.db')
        cursor = conexao.cursor()

        listar_central()
        id_busca_excluir = int(input("Digite o id da central que deseja excluir: "))

        cursor.execute(f''' DELETE FROM central_distribuicao WHERE id = {id_busca_excluir}''')
        conexao.commit()
        conexao.close()
    except ValueError:
        print("O ID deve ser um número.")
    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)
    except Exception as erro:
        print("Erro:", erro) 

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

            opcao = input("Escolha uma opçã0: ") 

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