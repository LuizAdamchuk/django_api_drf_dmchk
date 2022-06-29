# Back-end Django - DRF

O objetivo deste projeto é criar uma API Rest que utilizará os dados do projeto
[Space Flight News](https://api.spaceflightnewsapi.net/v3/documentation), uma api pública com informações sobre voos espaciais.

- Acessando o projeto: localhost:8000/

## Tecnologiais Utilizadas

- Django
- Django Rest Framework
- Django Crontab
- Postgresql
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

### URLs:

- http://localhost:8000/

### INSOMNIA

\*Para testar as requisições

- Arquivo está dentro de api_sfn/insomniaReq basta importart no seu insomnia.

## DONE

- [x] Para alimentar o seu banco de dados você deve criar um script para armazenar os dados de todos os artigos na Space Flight News API;

- [x] Docker configurado no Projeto para facilitar o Deploy da equipe de DevOps;

- [ ] Configurar um sistema de alerta se houver algum falha durante a sincronização dos artigos;

- [x] Descrever a documentação da API;
