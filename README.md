# Eventex
Sistema de Eventos encomendado pela Morena.

## Como desenvolver?
1. Clone o repositório.
2. Crie um virtualenv em Python 3.5
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6 Execute os testes. 

```console
git clone git@github.com:gutonovaes19/eventex
cd wttd
python -m venv .wtdd
source .wtdd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
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