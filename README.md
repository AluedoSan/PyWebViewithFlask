# 💰 PWV - Projeto WebView com Flask e SQLite

Este é um projeto simples de aplicação web feita com **Flask** e interface desktop usando **PyWebView**, utilizando **SQLite3** como banco de dados. Ele serve como base para um sistema de controle financeiro com caixinhas, tags e usuários.

---

## 🧱 Estrutura do Projeto

pwv/
├── tutorial.db # Banco de dados SQLite
├── init_db.py # Script para criar as tabelas
├── requirements.txt # Dependências do projeto
├── venv/ # Ambiente virtual (opcional)
└── src/
├── main.py # Aplicação Flask principal
├── static/ # Arquivos estáticos (CSS, JS, etc.)
└── templates/ # Templates HTML (Jinja2)

---

## 🛠️ Como rodar o projeto

### 1. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/seu-usuario/pwv.git
cd pwv

```
### 2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
```
### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 4. Crie o banco de dados (apenas a primeira vez):
```bash
python init_db.py
```
### 5. Rode a aplicação:
```bash
python src/main.py
```

📦 Banco de Dados

O banco tutorial.db contém as seguintes tabelas:

- user: informações dos usuários (nome, senha, email, data de nascimento)

- bancos: registros de bancos ou contas com nome, total e descrição

- caixinhas: descrições financeiras, valores e data

- tags: sistema de tags com nome e descrição

🌐 Tecnologias usadas

- Python 3.x

- Flask

- PyWebView

- SQLite3

- HTML/CSS (com Jinja2 nos templates)

📌 Próximas funcionalidades

- Sistema de login/autenticação

- Interface para inserir e visualizar transações

- Filtros por data/tags

- Exportar dados para CSV ou PDF

📄 Licença

Este projeto é livre para fins de estudo e aprendizado.

---

Se quiser personalizar com seu nome, GitHub, ou adicionar badges (ex: Python version, build passing), posso te ajudar com isso também.

Quer que eu gere também o `requirements.txt` certinho com os pacotes que você já usou?
