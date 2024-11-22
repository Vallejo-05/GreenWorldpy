###GreenWorld: Sistema de Consumo Consciente de Energia
Este código implementa uma plataforma simples e funcional chamada GreenWorld, focada em ajudar os usuários a monitorarem seu consumo de energia elétrica e fornecer recomendações personalizadas para otimizar esse consumo.

##Funcionalidades
Cadastro de Usuários
Os usuários podem se registrar utilizando um e-mail e senha. O cadastro é salvo em um banco de dados MongoDB.

##Login de Usuários
Após o cadastro, o sistema permite que os usuários façam login para acessar suas informações e adicionar seu consumo mensal de energia.

##Registro do Consumo de Energia
Durante a sessão, o usuário informa seu consumo de energia em kWh, que é registrado no sistema.

##Geração de Recomendações
Com base no consumo registrado, o sistema gera uma recomendação personalizada para ajudar o usuário a reduzir desperdícios e promover hábitos mais sustentáveis.

Armazenamento no MongoDB
Todas as informações de usuários, consumos e recomendações são armazenadas em um banco de dados MongoDB.

Logs de Atividades
O código registra logs de todas as atividades, como cadastros, logins e atualizações de consumo, em um arquivo local para facilitar o monitoramento.

Objetivo
O objetivo principal deste código é incentivar o uso consciente de energia elétrica por meio de uma abordagem personalizada, promovendo sustentabilidade e eficiência energética.

Pré-requisitos
Python 3.x
MongoDB instalado e em execução na porta padrão localhost:27017
Biblioteca pymongo instalada (pip install pymongo)
Como Executar
Configuração do Banco de Dados
Certifique-se de que o MongoDB esteja em execução. O banco de dados utilizado será greenworld e a coleção usuarios.

Execução do Script
Execute o script no terminal com o comando:

bash
Copiar código
python greenworld.py
Interação com o Sistema

Escolha entre as opções no menu:
Cadastrar: Insira seu e-mail e senha para criar uma conta.
Login: Acesse sua conta e informe seu consumo mensal para receber recomendações.
Sair: Encerre o programa.
Fluxo de Operações
O usuário pode se cadastrar no sistema.
Após o login, o sistema solicita o consumo mensal de energia (em kWh).
Com base no consumo informado:
Valores acima de 500 kWh geram alertas para reduzir o uso de eletrodomésticos e ar-condicionado.
Valores entre 200 e 500 kWh sugerem ações como a troca de lâmpadas por LEDs.
Consumos abaixo de 200 kWh recebem mensagens parabenizando o usuário pela eficiência.
Estrutura de Dados
Usuários (usuarios):
json
Copiar código
{
  "_id": "ObjectId",
  "email": "exemplo@email.com",
  "senha": "senha123",
  "consumo": 350,
  "recomendacao": "Troque lâmpadas por LEDs e use menos eletrônicos."
}
Logs
As operações do sistema, como cadastros, logins e atualizações de consumo, são registradas no arquivo greenworld_logs.txt para fins de monitoramento.

Exemplo de Uso
plaintext
Copiar código
Bem vindo a GreenWorld! 
1 - Cadastrar
2 - Login
3 - Sair
Escolha uma opção: 1
Digite seu e-mail: usuario@email.com
Digite sua senha: senha123
Cadastro concluído! Por favor, faça login.

Escolha uma opção: 2
Digite seu e-mail: usuario@email.com
Digite sua senha: senha123
Login realizado com sucesso!
Digite seu consumo mensal de energia (em kWh): 400
Bem-vindo(a), usuario@email.com!
Seu consumo mensal de energia: 400 kWh
Recomendação personalizada: Troque lâmpadas por LEDs e use menos eletrônicos.
A plataforma GreenWorld é uma ferramenta prática e educativa que promove o uso consciente de energia, contribuindo para um futuro mais sustentável.





