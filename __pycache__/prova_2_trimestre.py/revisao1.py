import sqlite3


def inicializar_banco():
  """Cria o banco de dados e as tabelas com chave estrangeira."""
  conexao = sqlite3.connect("hospital.db")
  cursor = conexao.cursor()

  # Habilita o suporte a chaves estrangeiras no SQLite
  cursor.execute("PRAGMA foreign_keys = ON;")

  # Tabela de Hospitais
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id_hospital INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_hospital TEXT NOT NULL,
            cidade_hospital TEXT NOT NULL
        )
    """)

  # Tabela de Médicos com Chave Estrangeira
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_medico TEXT NOT NULL,
            crm_medico TEXT NOT NULL UNIQUE,
            id_hospital INTEGER,
            FOREIGN KEY (id_hospital) REFERENCES hospitais (id_hospital)
        )
    """)

  conexao.commit()
  conexao.close()

def cadastrar_hospital():
  """Cadastra um novo hospital."""
  conexao = sqlite3.connect("hospital.db")
  cursor = conexao.cursor()

  print("\n--- CADASTRO DE HOSPITAL ---")
  nome = input("Digite o nome do hospital: ")
  cidade = input("Digite a cidade do hospital: ")

  try:
    cursor.execute(
        "INSERT INTO hospitais (nome_hospital, cidade_hospital) VALUES (?, ?)",
        (nome, cidade),
    )
    conexao.commit()
    print("Hospital cadastrado com sucesso!")
  except sqlite3.Error as e:
    print(f"Erro ao cadastrar hospital: {e}")
  finally:
    conexao.close()


def listar_hospitais():
  """Lista todos os hospitais cadastrados."""
  conexao = sqlite3.connect("hospital.db")
  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM hospitais")
  hospitais = cursor.fetchall()

  if not hospitais:
    print("\nNenhum hospital encontrado!")
    conexao.close()
    return False
  else:
    print("\n--- LISTA DE HOSPITAIS ---")
    for h in hospitais:
      print(f"ID: {h[0]} | Nome: {h[1]} | Cidade: {h[2]}")
    print("-" * 30)
    conexao.close()
    return True


def cadastrar_medico():
  """Cadastra um médico vinculando-o a um ID de hospital existente (com tratamento de erro)."""
  # Verifica se existem hospitais cadastrados antes de prosseguir
  if not listar_hospitais():
    print("Cadastre um hospital primeiro para poder vincular o médico.")
    return

  conexao = sqlite3.connect("hospital.db")
  cursor = conexao.cursor()
  cursor.execute("PRAGMA foreign_keys = ON;")

  print("\n--- CADASTRO DE MÉDICO ---")
  nome = input("Digite o nome do médico: ")
  crm = input("Digite o CRM do médico: ")
 

  try:
    id_hospital = int(
        input("Digite o ID do hospital onde o médico será vinculado: ")
    )
  except ValueError:
    print("Erro: O ID do hospital deve ser um número inteiro.")
    conexao.close()
    return

  # Verifica se o hospital informado realmente existe
  cursor.execute(
      "SELECT id_hospital FROM hospitais WHERE id_hospital = ?", (id_hospital,)
  )
  if not cursor.fetchone():
    print(
        f"Erro: O hospital com ID {id_hospital} não existe! Cadastro cancelado."
    )
    conexao.close()
    return

  try:
    cursor.execute(
        """INSERT INTO medicos (nome_medico, crm_medico, especialidade_medico, id_hospital) 
               VALUES (?, ?, ?, ?)""",
        (nome, crm, id_hospital),
    )
    conexao.commit()
    print("Médico cadastrado com sucesso!")
  except sqlite3.IntegrityError as e:
    print(f"Erro de integridade (CRM duplicado ou ID inválido): {e}")
  except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")
  finally:
    conexao.close()


def listar_medicos():
  """Lista todos os médicos cadastrados."""
  conexao = sqlite3.connect("hospital.db")
  cursor = conexao.cursor()

  cursor.execute("""
        SELECT m.id_medico, m.nome_medico, m.crm_medico, m.especialidade_medico, h.nome_hospital 
        FROM medicos m
        JOIN hospitais h ON m.id_hospital = h.id_hospital
    """)
  medicos = cursor.fetchall()

  if not medicos:
    print("\nNenhum médico encontrado!")
  else:
    print("\n--- LISTA DE MÉDICOS ---")
    for m in medicos:
      print(
          f"ID: {m[0]} | Nome: {m[1]} | CRM: {m[2]} | Especialidade: {m[3]} |"
          f" Hospital: {m[4]}"
      )
    print("-" * 30)
  conexao.close()


def excluir_hospital():
  """Exclui um hospital pelo ID."""
  conexao = sqlite3.connect("hospital.db")
  cursor = conexao.cursor()
  cursor.execute("PRAGMA foreign_keys = ON;")

  listar_hospitais()
  try:
    id_hospital = int(input("Digite o ID do hospital que deseja excluir: "))
  except ValueError:
    print("ID inválido.")
    conexao.close()
    return

  cursor.execute(
      "SELECT * FROM hospitais WHERE id_hospital = ?", (id_hospital,)
  )
  if not cursor.fetchone():
    print("Hospital não encontrado!")
    conexao.close()
    return

  try:
    cursor.execute("DELETE FROM hospitais WHERE id_hospital = ?", (id_hospital,))
    conexao.commit()
    print("Hospital excluído com sucesso!")
  except sqlite3.IntegrityError:
    print(
        "Erro: Não é possível excluir este hospital pois há médicos vinculados a"
        " ele."
    )
  finally:
    conexao.close()


def menu():
  inicializar_banco()
  while True:
    print("\n--- SISTEMA DE HOTAIS E MÉDICOS ---")
    print("1- Cadastrar Hospital")
    print("2- Listar Hospitais")
    print("3- Cadastrar Médico (com FK)")
    print("4- Listar Médicos")
    print("5- Excluir Hospital")
    print("6- Sair")

    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
      cadastrar_hospital()
    elif opcao == "2":
      listar_hospitais()
    elif opcao == "3":
      cadastrar_medico()
    elif opcao == "4":
      listar_medicos()
    elif opcao == "5":
      excluir_hospital()
    elif opcao == "6":
      print("Encerrando sistema!")
      break
    else:
      print("Opção inválida!")


menu()