# Django Todo List

Este é um projeto simples de **Todo List** desenvolvido como parte de um estudo de **Django**, explorando conceitos básicos e boas práticas no desenvolvimento de aplicações web. O objetivo principal é aprender e aplicar funcionalidades essenciais do framework Django, como modelos, views, templates e o uso de bibliotecas externas para melhorar a experiência do desenvolvimento.

## Funcionalidades Implementadas

- **Criação de Tarefas:** Página para adicionar novas tarefas com suporte a formulários estilizados usando Crispy Forms.
- **Listagem de Tarefas:** Exibição de tarefas utilizando **Class-Based Views (CBVs)**.
- **Gerenciamento de Variáveis de Ambiente:** Uso das bibliotecas `python-decouple` e `dj-database-url` para facilitar o manuseio de configurações sensíveis.
- **Estilização:** Integração com **Crispy Forms** e **Bootstrap 5** para criar formulários e layouts responsivos.
- **Formatação de Código:** O código segue o padrão **PEP8**, formatado automaticamente com o **Black**.

## Tecnologias Utilizadas

- **Django:** Framework principal para desenvolvimento web.
- **Crispy Forms + Bootstrap 5:** Para estilização de formulários e templates.
- **Python Decouple e dj-database-url:** Para gerenciar variáveis de ambiente e configurações do banco de dados.
- **SQLite:** Banco de dados padrão para prototipagem.

## Estrutura do Projeto

O projeto segue uma organização típica do Django. Algumas pastas e arquivos relevantes incluem:

- **`todos/`**: Aplicação principal contendo modelos, views e templates.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`.vscode/settings.json`**: Configurações adicionais para o VSCode.(Optei por incluir nesse repositório como documentação)
- **`manage.py`**: Ponto de entrada para comandos do Django.