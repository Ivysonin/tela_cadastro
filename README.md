# 🚀 API de Autenticação e Usuários

API REST desenvolvida em **Python + Flask** para gerenciamento de **autenticação** e **perfil de usuários**. O projeto segue separação clara de responsabilidades entre **Auth** (autenticação) e **User** (domínio do usuário), com foco em boas práticas, validação de dados e segurança.

---

## 🎯 Objetivo

Fornecer uma API simples, limpa e escalável para:

* Registro de usuários
* Autenticação (login/logout)
* Gerenciamento de perfil do usuário autenticado

Este projeto é voltado para estudo e prática de **arquitetura backend**, **validação**, **segurança** e **organização de código**.

---

## 🛠 Tecnologias Utilizadas

* Python
* Flask
* Flask-Login
* Marshmallow (validação de dados)
* SQLAlchemy
* SQLite
* Werkzeug (hash de senha)

---


## 🔌 **Como Rodar o Projeto**

### 1. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um `.env`:

```
SECRET_KEY='chave_secreta'
DATABASE_URI='sqlite:///database.db'

# configurações de sessão/cookies
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE="Lax"
```

### 4. Inicializar o banco

```bash
flask db upgrade
```

### 5. Executar o servidor

```bash
flask run
```

---

## 📌 **Endpoints disponíveis**

### 🔐 Autenticação

| Método | URL            | Descrição              |
| ------ | -------------- | ---------------------- |
| POST   | /auth/register | Registra novo usuário  |
| POST   | /auth/login    | Login do usuário       |
| POST   | /auth/logout   | Logout do usuário      |

---

### 👤 Usuário

| Método | URL             | Descrição              |
| ------ | --------------- | ---------------------- |
| GET    | /users/perfil   | Informações do usuário |
| PUT    | /users/perfil   | Atualiza informações   |

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](./LICENSE).
