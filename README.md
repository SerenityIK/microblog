# Microblog Flask-app

## Features

*   Material theme
*   Private Messages
*   Search with elasticsearch
*   Redis background tasks
*   API with security tokens

## Quick Start

**Get docker contaier**:

  `docker pull docker.pkg.github.com/serenityik/microblog/microblog:latest`

**Run command**:

  `docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key
  -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true
  -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password>
  --link mysql:dbserver
  -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog
  --link elasticsearch:elasticsearch
  -e ELASTICSEARCH_URL=http://elasticsearch:9200
  microblog:latest`

## API usage

**User creation**:

  `POST http://localhost:5000/api/users username=<username> password=<password> password=<password> email=<email>`

**Generate user token**:

  `--auth <username>:<password> POST http://localhost:5000/api/tokens`

**User update**:

  `PUT http://localhost:5000/api/users/<id> "about_me=Hello, my name is <name>!" "Authorization:Bearer <token>"`

**Get users list**:

  `GET http://localhost:5000/api/users "Authorization:Bearer <token>"`

**Get user followers**:

  `GET http://localhost:5000/api/users/<id>/followers "Authorization:Bearer <token>"`
