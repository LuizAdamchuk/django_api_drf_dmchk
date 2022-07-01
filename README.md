# Back-end Django - DRF

- [PokeApi](https://pokeapi.co/);
- [Space Flight News API](https://www.spaceflightnewsapi.net/)

## Tecnologiais Utilizadas

- Django
- Django Rest Framework
- Django Crontab
- PostgreSQL
- Docker

## Instalação do Projeto

- Passo 1:

```
git clone https://github.com/LuizAdamchuk/django_api_drf_dmchk.git
cd django_api_drf_dmchk
```

- Passo 2:

```
docker-compose up -d
```

- Passo 3 _(para encerrar)_:

```
docker-compose down
```

# POKE-API DONE

- http://localhost:8000/pokemon/

- [x] Bate na [PokeApi](https://pokeapi.co/);

- [x] Possibilita procurar pelo nome por um input em tela;

- [x] Retorna habilidades em ordem alfabetica;

- [x] Começo de validação de erros;

- [x] Docker configurado no Projeto para facilitar o Deploy da equipe de DevOps;

## BLOG-API DONE

- http://localhost:8000/blog/
- http://localhost:8000/admin/ _Para usar o admin é necessário criar um super user (abaixo como criar)_

- [x] Cron pegar dados da api [Space Flight News API](https://www.spaceflightnewsapi.net/);

- [x] Dados salvos no PostgreSQL;

- [x] Docker configurado no Projeto para facilitar o Deploy da equipe de DevOps;

- [x] Configurar um sistema de alerta se houver algum falha durante a sincronização dos artigos;

- [x] Descrever a documentação da API;

### URLs:

- http://localhost:8000/
- http://localhost:8000/blog/
- http://localhost:8000/pokemon/
- http://localhost:8000/admin/

### INSOMNIA

\*Para testar as requisições

- Arquivo está dentro de api_sfn/insomniaReq basta importart no seu insomnia.

### Criar super user django python

Ver os containers que estao rodando:

```
docker container ls (ver o id do container web)
```

entrar no container:

```
docker exec -it <idcontainer> bash
```

criar super user:

```
python manage.py createsuperuser
```

acessar a url http://localhost:8000/admin/ colocar as credencias criadas

### Mudar credencias do banco/mailtrap

- Mude as credencias default _(Cria o .env com os comandos abaixo e cadastre suas credenciais)_:

```
cd config
touch .env
echo "DATABASE_NAME=\nDATABASE_USER=\nDATABASE_PASS=\nMAILTRAP_HOST=\nMAILTRAP_PORT=\nMAILTRAP_HOST_USER=\nMAULTRAP_HOST_PASS=\n" > .env
```

_Descomente no arquivo Dockerfile na linha:_

```
# COPY ./config/.env ./config
```
