# Eventex
Sistema de Eventos encomendado pela Morena.
Revisado em 27/01/2018
[![Build Status](https://travis-ci.org/gutonovaes19/eventex.svg?branch=master)](https://travis-ci.org/gutonovaes19/eventex)

## Como desenvolver?
1. Clone o repositório.
2. Crie um virtualenv em Python 3.5
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6 Execute os testes. 
6.1 Macete manage.bat 

```console
git clone git@github.com:gutonovaes19/eventex
cd wttd
python -m venv .wtdd
source .wtdd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
manage.bat (@python "%VIRTUAL_ENV%\..\manage.py" %*)
```
## Como fazer o Deploy?
1. Crie uma Instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECURET_KEY segura para a instancia
4. Defina Debug = false
5. Configure o serviço de e-mail.
6. Envie o código para o heroku

```Console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:Debug=False
#configuro o email
git push heroku master --force

```

## Lembrete para Testes
1. Conferir configuração de e-mail remetente
