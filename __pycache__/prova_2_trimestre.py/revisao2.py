import sqlite3


def inicializar_banco():
  """Cria o banco de dados 'cinema.db' e as tabelas necessárias."""
  conexao = sqlite3.connect("cinema.db")
  cursor = conexao.cursor()

  # Habilita o suporte a chaves estrangeiras no SQLite
  cursor.execute("PRAGMA foreign_keys = ON;")

  # Tabela de Cinemas
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cinema TEXT NOT NULL,
            shopping TEXT NOT NULL
        )
    """)

  # Tabela de Salas com Chave Estrangeira
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER NOT NULL,
            capacidade INTEGER NOT NULL,
            id_cinema INTEGER,
            FOREIGN KEY (id_cinema) REFERENCES cinemas (id)
        )
    """)

  conexao.commit()
  conexao.close()


def cadastrar_cinema():
  """Função auxiliar para cadastrar cinemas (necessário antes de cadastrar salas)."""
  conexao = sqlite3.connect("cinema.db")
  cursor = conexao.cursor()

  print("\n--- CADASTRO DE CINEMA ---")
  nome = input("Digite o nome do cinema: ")
  shopping = input("Digite o shopping onde fica o cinema: ")

  try:
    cursor.execute(
        "INSERT INTO cinemas (nome_cinema, shopping) VALUES (?, ?)",
        (nome, shopping),
    )
    conexao.commit()
    print("Cinema cadastrado com sucesso!")
  except sqlite3.Error as e:
    print(f"Erro ao cadastrar cinema: {e}")
  finally:
    conexao.close()


def listar_cinemas():
  """Lista os cinemas cadastrados para consulta de IDs."""
  conexao = sqlite3.connect("cinema.db")
  cursor = conexao.cursor()

  cursor.execute("SELECT id, nome_cinema, shopping FROM cinemas")
  cinemas = cursor.fetchall()

  if not cinemas:
    print("\nNenhum cinema cadastrado!")
    conexao.close()
    return False

  print("\n--- CINEMAS CADASTRADOS ---")
  for c in cinemas:
    print(f"ID: {c[0]} | Nome: {c[1]} | Shopping: {c[2]}")
  print("-" * 30)
  conexao.close()
  return True


def cadastrar_sala():
  """Cadastra uma sala protegendo os campos numéricos com try/except ValueError."""
  if not listar_cinemas():
    print("Você precisa cadastrar pelo menos um cinema antes de criar salas.")
    return

  print("\n--- CADASTRO DE SALA ---")

  # Proteção com try/except ValueError para campos numéricos
  try:
    numero_sala = int(input("Digite o número da sala: "))
    capacidade = int(input("Digite a capacidade de pessoas da sala: "))
    id_cinema = int(
        input("Digite o ID do cinema onde esta sala está localizada: ")
    )
  except ValueError:
    print(
        "\n[Erro] Entrada inválida! Os campos de número da sala, capacidade e ID"
        " devem conter apenas números inteiros."
    )
    return

  conexao = None
  try:
    conexao = sqlite3.connect("cinema.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Verifica se o ID do cinema informado realmente existe
    cursor.execute("SELECT id FROM cinemas WHERE id = ?", (id_cinema,))
    if not cursor.fetchone():
      print(
          f"\n[Erro] O cinema com ID {id_cinema} não existe! Cadastro"
          " cancelado."
      )
      return

    # Insere a sala caso tudo esteja correto
    cursor.execute(
        """INSERT INTO salas (numero_sala, capacidade, id_cinema) 
               VALUES (?, ?, ?)""",
        (numero_sala, capacidade, id_cinema),
    )
    conexao.commit()
    print("\nSala cadastrada com sucesso!")

  except sqlite3.Error as e:
    print(f"\nErro no banco de dados: {e}")
  finally:
    if conexao:
      conexao.close()


def listar_salas():
  """Lista todas as salas utilizando fetchall() com os dados do cinema correspondente."""
  conexao = sqlite3.connect("cinema.db")
  cursor = conexao.cursor()

  try:
    # Utiliza JOIN para trazer o nome do cinema junto com os dados da sala
    cursor.execute("""
            SELECT s.id, s.numero_sala, s.capacidade, c.nome_cinema, c.shopping 
            FROM salas s
            JOIN cinemas c ON s.id_cinema = c.id
        """)
    salas = cursor.fetchall()

    if not salas:
      print("\nNenhuma sala cadastrada no sistema!")
    else:
      print("\n--- LISTA DE TODAS AS SALAS ---")
      for sala in salas:
        print(
            f"ID Sala: {sala[0]} | Sala Nº: {sala[1]} | Capacidade:"
            f" {sala[2]} lugares | Cinema: {sala[3]} ({sala[4]})"
        )
      print("-" * 50)
  except sqlite3.Error as e:
    print(f"Erro ao listar salas: {e}")
  finally:
    conexao.close()


def menu():
  """Menu interativo do sistema."""
  inicializar_banco()
  while True:
    print("\n--- SISTEMA DE CINEMAS ---")
    print("1- Cadastrar Cinema")
    print("2- Listar Cinemas")
    print("3- Cadastrar Sala")
    print("4- Listar todas as Salas")
    print("5- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      cadastrar_cinema()
    elif opcao == "2":
      listar_cinemas()
    elif opcao == "3":
      cadastrar_sala()
    elif opcao == "4":
      listar_salas()
    elif opcao == "5":
      print("Encerrando o sistema. Até logo!")
      break
    else:
      print("Opção inválida! Tente novamente.")



menu()