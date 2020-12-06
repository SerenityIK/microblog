# Microblog Flask-app


**Features:**
-----------
* Material theme
* Private Messages
* Search with elasticsearch
* Redis background tasks

**Quick Start**
-----------
* Get docker contaier:

  `docker pull docker.pkg.github.com/serenityik/microblog/microblog:0.1`
* Run coommand:

  `docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key
  -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true
  -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password>
  --link mysql:dbserver
  -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog
  --link elasticsearch:elasticsearch
  -e ELASTICSEARCH_URL=http://elasticsearch:9200
  microblog:0.1`
