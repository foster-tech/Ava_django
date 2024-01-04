# comandos utils

- Para instalar con pip env
> pipenv --python=3.10 install

- Para entrar na maquina virtual
> pipenv shell

- Para add tabelas DB
> pipenv run python manage.py migrate

- Para atualizar as traduções
> django-admin compilemessages

- Para correr servidor
> pipenv run python manage.py runserver

- Gerar requirements.txt
> pipenv run pip freeze > requirements.txt

# Structure