# 🐶 Find A Friend

**Find A Friend** é uma API desenvolvida em Python e Flask para facilitar o processo de adoção de PETs. O projeto implementa a Arquitetura MVC, explorando diversos conceitos fundamentais para aplicações escaláveis e bem estruturadas.

## ⚙️ Funcionalidades

- 📝 Registrar uma pessoa adotando um PET.
- 🔍 Listar todos os PETs cadastrados.
- ❌ Deletar um PET do sistema.
- 👤 Retornar informações de uma pessoa e seu respectivo PET.

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python**: Linguagem de programação utilizada para o desenvolvimento da API.
- 🌐 **Flask**: Framework web utilizado para a criação e estruturação da API.
- 📦 **SQLite**: Banco de dados leve e eficiente utilizado no projeto.
- 🗄️ **SQLAlchemy**: Biblioteca para manipulação de banco de dados.
- ⚙️ **Werkzeug**: Biblioteca WSGI utilizada para serviços web.
- 📏 **Pydantic**: Biblioteca para validação de dados.
- 🛡️ **Pylint**: Ferramenta para análise de qualidade do código.
- 🧪 **Pytest**: Framework para testes.
- 🌱 **Virtualenv**: Ferramenta para criação de ambientes virtuais isolados.
- ✅ **Pre-commit**: Ferramenta para validações automáticas no código antes de cada commit.

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/joschonarth/find-a-friend
   cd find-a-friend
   ```

2. **Crie um ambiente virtual**:

   ```bash
   virtualenv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicialize o banco de dados**:

    Execute o script `schema.sql` na pasta `init` para configurar as tabelas e inserir os dados iniciais:

    ```bash
    sqlite3 database.db < schema.sql
    ```

5. **Execute o servidor**:

   ```bash
   python run.py
   ```

A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🌐 Estrutura do Projeto

O projeto segue o padrão de Arquitetura MVC:

- **Model**: Representação dos dados e interações com o banco de dados.
- **View**: Responsável por retornar respostas HTTP e interações com os clientes.
- **Controller**: Contém a lógica de negócio e faz a ponte entre o Model e a View.

## 🌍 Deploy

O projeto foi implantado utilizando a plataforma Render, que oferece hospedagem simples e escalável para aplicações web. Acesse a aplicação no ambiente de produção através do link abaixo:

👉 [Find A Friend - Deploy na Render](https://find-a-friend.onrender.com)

## 🔗 Rotas da API

### PETs

- 🐾 **GET** `/pets` - Lista todos os PETs cadastrados.
- 🗑️ **DELETE** `/pets` - Deleta um PET do sistema.

### Pessoas

- ✍️ **POST** `/people` - Cria o registro de uma pessoa.

   **Body**:

   ```json
   {
      "first_name": "<string>",
      "last_name": "<string>",
      "age": <int>,
      "pet_id": <int>
   }
   ```

- 👤 **GET** `/people/:person_id` - Retorna informações sobre uma pessoa e seu respectivo PET.

   **Path Variable**:

   `person_id` (int): ID da pessoa.

## ✅ Testes

O projeto inclui uma série de testes unitários e de integração para garantir a qualidade do código:

1. **Execute os testes**:

   ```bash
   pytest
   ```

2. **Visualize mais detalhes e mensagens do teste**:

   ```bash
   pytest -s -v
   ```

## Contribuições 🌟

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue com sugestões ou enviar um pull request com melhorias.

## 📞 Contato 

<div>
    <a href="https://www.linkedin.com/in/joschonarth/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:joschonarth@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>