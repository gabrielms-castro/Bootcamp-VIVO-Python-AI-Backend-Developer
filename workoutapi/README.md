Para rodar localmente:

```Python
pip install -r requirements.txt
```

```Docker
docker-compose up -d
```

```Makefile
make create-migrations d="init_db"
make run-migrations
```

Rodar o servidor
```Makefile
make run
```