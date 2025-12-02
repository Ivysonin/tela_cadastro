# 📋 Tela Cadastro

Projeto de um sistema web para cadastro de usuários, desenvolvido com Python e Flask. O principal objetivo é praticar a lógica de cadastro, validação de dados e a interação com um banco de dados.

## 🚀 Funcionalidades

- Cadastro de usuários com validação de dados

## 🛠 Tecnologias Utilizadas

- Python
- Flask
- Flask-WTF (para formulários e validação)
- Flask-Login (para controle de sessão)
- Flask-Bcrypt (para hash de senhas)
- SQLite (via SQLAlchemy)
- HTML + CSS
- Bootstrap (para estilização dos templates)

## ⚙️ Variáveis de Ambiente

Antes de rodar a aplicação, crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URI=sqlite:///database.db
```

## 💻 Como Rodar Localmente

```bash
# clone o repositorio
git clone https://github.com/Ivysonin/tela_cadastro.git

# Crie o ambiente virtual
python -m venv venv

# Ative no Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python run.py
```


## 📖 Aprendizados

- Estruturação de aplicações Flask
- Manipulação de formulários e envio de dados via POST
- Validação customizada para evitar duplicidade de dados
- Hash de senhas para segurança usando Flask-Bcrypt
- Integração com banco de dados usando SQLite
- Uso de variáveis de ambiente para manter configurações sensíveis fora do código

## 📸 Imagem
![Imagem tela cadastro](https://github.com/user-attachments/assets/67b21400-91fc-441f-9f14-827cc12886bf)

## 📄 Licença

Este projeto está licenciado sob os termos da [Licença MIT](./LICENSE).
