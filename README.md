🌱 ##GreenWorld: Plataforma de Consumo Consciente e Sustentável 🌍
GreenWorld é uma aplicação desenvolvida com o objetivo de promover um futuro mais sustentável, incentivando os usuários a monitorarem seu consumo de energia elétrica e adotarem práticas mais ecológicas. Com base no consumo de energia dos usuários, a plataforma gera recomendações personalizadas para otimizar o uso de recursos e reduzir o impacto ambiental.

🚀 Funcionalidades
A plataforma GreenWorld permite que os usuários se cadastrem, façam login e registrem seu consumo de energia. Após o login, são fornecidas recomendações personalizadas para ajudar a reduzir o consumo e melhorar a eficiência energética.

Principais funcionalidades:

Cadastro de usuário: O usuário pode criar uma conta informando seu e-mail e senha.
Login: A plataforma permite que os usuários façam login com as credenciais criadas.
Recomendações de consumo: A cada login, o usuário insere seu consumo mensal de energia (em kWh), e com base nisso, a plataforma gera recomendações sobre como reduzir o consumo de energia.
Armazenamento de dados: Todos os dados dos usuários, como e-mail, senha, consumo e recomendações, são armazenados em um banco de dados MongoDB.
⚙️ Tecnologias Utilizadas
MongoDB: Banco de dados NoSQL utilizado para armazenar os dados dos usuários, incluindo e-mail, senha, consumo de energia e recomendações personalizadas.
Python: A aplicação foi desenvolvida em Python, utilizando bibliotecas como pymongo para interação com o banco de dados e logging para registro de logs e monitoramento da aplicação.
📋 Como Rodar o Projeto
1. Instalação do MongoDB
Certifique-se de que o MongoDB está instalado e em execução na sua máquina. Você pode seguir a documentação oficial do MongoDB para instalar e configurar o MongoDB corretamente.

2. Instalar Dependências
Instale a biblioteca pymongo utilizando o seguinte comando:

bash
Copiar código
pip install pymongo
3. Configuração do Banco de Dados
O código conecta automaticamente ao banco de dados MongoDB na URL mongodb://localhost:27017/ e cria a base de dados greenworld, onde os dados dos usuários serão armazenados.

4. Executando a Aplicação
Após garantir que o MongoDB está em execução, execute o script Python:

bash
Copiar código
python greenworld.py
5. Interação com a Plataforma
O usuário poderá interagir com a plataforma através de um menu no terminal:

Cadastro de novo usuário: Ao selecionar a opção de cadastro, o usuário informará seu e-mail e senha.
Login: Após o cadastro, o usuário pode fazer login inserindo o e-mail e a senha criados.
Inserção do consumo de energia: Após o login, o usuário deve inserir seu consumo mensal de energia (em kWh), e a plataforma fornecerá recomendações para otimizar esse consumo.
Encerramento da plataforma: O usuário pode escolher encerrar a plataforma a qualquer momento.
🔧 Estrutura do Código
Função conectar_db(): Responsável por estabelecer a conexão com o banco de dados MongoDB.
Função cadastrar(): Permite o cadastro de um novo usuário verificando se o e-mail já está registrado.
Função login(): Realiza a autenticação do usuário, comparando o e-mail e a senha fornecidos com os dados no banco de dados.
Função gerar_recomendacao(): Gera recomendações personalizadas com base no consumo de energia fornecido pelo usuário.
Função atualizar_consumo(): Atualiza os dados do usuário com o consumo informado e a recomendação gerada.
Função exibir_recomendacao(): Exibe o consumo mensal de energia e as recomendações personalizadas para o usuário.
📝 Logs
A plataforma gera logs de todas as ações executadas, como cadastro, login, e atualizações no banco de dados, para ajudar no monitoramento e solução de problemas. Esses logs são armazenados em um arquivo chamado greenworld_logs.txt.

📧 Contato
Caso tenha dúvidas ou sugestões, entre em contato com o desenvolvedor através do e-mail: greenworld@suporte.com

🛠️ Contribuindo
Sinta-se à vontade para contribuir com este projeto! Se você quiser sugerir melhorias ou corrigir problemas, fique à vontade para abrir uma pull request.



