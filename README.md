# Django Todo List

Este é um projeto simples de **Todo List** desenvolvido como parte de um estudo de **Django**, explorando conceitos básicos e boas práticas no desenvolvimento de aplicações web. O objetivo principal é aprender e aplicar funcionalidades essenciais do framework Django, como modelos, views, templates e o uso de bibliotecas externas para melhorar a experiência do desenvolvimento.

## Screenshots

![home.png](/screenshots/home.png)
![new_task.png](/screenshots/new_task.png)
![delete.png](/screenshots/delete.png)

## Funcionalidades Implementadas

- **Criação de Tarefas:** Página para adicionar novas tarefas com formulários estilizados usando **Crispy Forms**.
- **Listagem de Tarefas:** Exibição de tarefas utilizando **Class-Based Views (CBVs)**.
- **Edição e Exclusão:** Tarefas podem ser atualizadas ou removidas diretamente na interface.
- **Finalização de Tarefas:** Utilizando o padrão **Fat Model Skinny View** para lógica de negócios.
- **Gerenciamento de Variáveis de Ambiente:** Uso das bibliotecas `python-decouple` e `dj-database-url` para facilitar o manuseio de configurações sensíveis.
- **Estilização:** Integração com **Crispy Forms** e **Bootstrap 5** para criar formulários e layouts responsivos.
- **Template Inheritance:** Uso de herança de templates para criar uma interface consistente.

## Tecnologias Utilizadas

- **Django:** Framework principal para desenvolvimento web.
- **Crispy Forms + Bootstrap 5:** Para estilização de formulários e templates.
- **Python Decouple e dj-database-url:** Para gerenciar variáveis de ambiente e configurações do banco de dados.
- **SQLite:** Banco de dados padrão para prototipagem.
- **HTML Template Inheritance:** Para reutilização de código nos templates.

## Estrutura do Projeto

O projeto segue uma organização típica do Django. Algumas pastas e arquivos relevantes incluem:

- **`todos/`**: Aplicação principal contendo modelos, views e templates.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`.vscode/settings.json`**: Configurações adicionais para o VSCode.(Optei por incluir nesse repositório como documentação)
- **`manage.py`**: Ponto de entrada para comandos do Django.

## Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/Moscarde/django-todo.git
cd django-todo
```
2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

source venv/bin/activate 
# No Windows: venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Configure as variáveis de ambiente no arquivo `.env` (use `.env.example` como referência).
5. Aplique as migrações:
```bash
pip install -r requirements.txt
```
6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```
7. Acesse o projeto no navegador: http://localhost:8000.