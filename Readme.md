📌 Newsletter Subscription App

Este projeto é uma aplicação web simples desenvolvida em Flask que permite:

📥 Registrar usuários interessados em participar de projetos freelancer.

📧 Enviar newsletters ou mensagens para todos os inscritos.

🌍 Coletar informações como nome, telefone, email, país, idiomas e gênero.

🚀 Funcionalidades

Formulário de inscrição com validações:

Nome completo

Telefone

Email (único no sistema)

País

Idiomas (até 3 opções, com possibilidade de inserir "Outro")

Gênero

Armazenamento dos dados em banco de dados (SQLite local ou PostgreSQL via variável DATABASE_URL).

Sistema de envio de mensagens via Flask-Mail (SMTP Gmail configurado).

Interface estilizada com Bootstrap 5.

🛠️ Tecnologias Utilizadas

Flask
 - Framework web em Python

Flask-SQLAlchemy
 - ORM para banco de dados

Flask-Mail
 - Envio de emails

Bootstrap 5
 - Estilização do front-end

📂 Estrutura do Projeto
project/
│── news_tiny/
│   │── app.py             # Aplicação principal Flask
│   │── parameters.py      # Listas de países e idiomas
│   │── templates/
│   │   ├── index.html     # Página de inscrição
│   │   └── send.html      # Página para envio de newsletters
│   │── static/
│   │   └── img/
│   │       └── logo.jpeg  # Logo usada no formulário
│
│── .gitignore             
│── requirements.txt       # Dependências do projeto
│── migration.py           # Script para criar DB
│── README.md              # Documentação