import pymongo
import logging

logging.basicConfig(filename='greenworld_logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Conexão com o banco de dados
def conectar_db():
    try:
        cliente = pymongo.MongoClient("mongodb://localhost:27017/")
        db = cliente["greenworld"]
        logging.info("Conexão com MongoDB bem-sucedida.")
        return db
    except pymongo.errors.ConnectionError as erro:
        logging.error(f"Erro ao conectar com MongoDB: {erro}")
        return None


# Cadastro de usuário
def cadastrar(db, email, senha):
    try:
        usuarios = db["usuarios"]

        if usuarios.find_one({"email": email}):
            print("E-mail já cadastrado.")
            logging.info(f"Tentativa de cadastro com e-mail já existente: {email}")
            return False

        usuarios.insert_one({
            "email": email,
            "senha": senha,
            "consumo": None,  # Consumo será preenchido após o login
            "recomendacao": None
        })
        print("Cadastro realizado com sucesso!")
        logging.info(f"Usuário cadastrado: {email}")
        return True
    except Exception as erro:
        logging.error(f"Erro ao cadastrar usuário: {erro}")
        return False


# Login do usuário
def login(db, email, senha):
    try:
        usuarios = db["usuarios"]
        usuario = usuarios.find_one({"email": email, "senha": senha})

        if usuario:
            print("Login realizado com sucesso!")
            logging.info(f"Login bem-sucedido: {email}")
            return usuario
        else:
            print("E-mail ou senha incorretos.")
            logging.warning(f"Falha no login: {email}")
            return None
    except Exception as erro:
        logging.error(f"Erro ao realizar login: {erro}")
        return None


# Gerar recomendação com base no consumo de energia (apenas exemplos de recomendações)
def gerar_recomendacao(consumo):
    if consumo > 500:
        return "Seu consumo de kWh está muito alto! Reduza o uso de ar condicionado e otimize o uso de eletrodomésticos."
    elif 200 < consumo <= 500:
        return "Seu consumo de kWh está acima do ideal! Comece a utilizar lâmpadas LEDs em sua casa e considere usar menos eletrônicos."
    else:
        return "Ótimo consumo! Continue monitorando seu uso."


# Atualizar consumo e recomendação do usuário
def atualizar_consumo(db, usuario, consumo):
    try:
        usuarios = db["usuarios"]
        recomendacao = gerar_recomendacao(consumo)

        usuarios.update_one(
            {"_id": usuario["_id"]},
            {"$set": {"consumo": consumo, "recomendacao": recomendacao}}
        )
        logging.info(f"Consumo e recomendação atualizados para {usuario['email']}.")
        return recomendacao
    except Exception as erro:
        logging.error(f"Erro ao atualizar consumo e recomendação: {erro}")
        return None

#Exibição de dados e recomendação do usuário
def exibir_recomendacao(usuario, recomendacao):
    print(f"\nBem-vindo(a), {usuario['email']}!")
    print(f"Seu consumo mensal de energia: {usuario['consumo']} kWh")
    print(f"Recomendação personalizada: {recomendacao}")


# Menu principal
def menu():
    db = conectar_db()
    if db is None:
        print("Erro ao conectar ao banco de dados. Programa encerrado.")
        return

    while True:
        print("\nBem vindo a GreenWorld! ")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            if cadastrar(db, email, senha):
                print("Cadastro concluído! Por favor, faça login.")
        elif opcao == "2":
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            usuario = login(db, email, senha)
            if usuario:
                consumo = int(input("Digite seu consumo mensal de energia (em kWh): "))
                recomendacao = atualizar_consumo(db, usuario, consumo)
                usuario["consumo"] = consumo
                exibir_recomendacao(usuario, recomendacao)
        elif opcao == "3":
            print("Encerrando a plataforma.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
