# PJ_003
Flaskを使用したTODOアプリの開発

# Directory Structure

```
PJ_003
 ├-- src\                       // App directory
 |    ├-- templates\            // HTML files
 |    |    └-- index.html
 |    ├-- app.py                // App File
 |    └-- .env                  // Config environement file
 ├-- Dockerfile
 ├-- requirements.txt
 └-- compose.yml
```

# Development Environement

Activate command

```shell
docker compose up -d --build
```

# Config Environement file

- Config debug Mode (DEBUG=True or False)

# Initialize database

First, Login todo-app container with the following command

```shell
docker exec -it todo-app bash
```

Second, Initialize database with the following command

```shell
flask db init
flask db migrade
flask db upgrade
```