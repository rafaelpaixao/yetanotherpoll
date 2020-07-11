# YAP Backend

## Instalation

1. Install Python 3, open a terminal and:

```
pip install pyenv
```

2. Create a little room for django and his friends:

```
pipenv install
```

## Setting up

1. If can use Postgres by setting a enviroment variable like:

```
pipenv run python manage.py migrate
```

2. and then run the command bellow. Or skip the last step and jump the SQLite train:

```
pipenv run python manage.py migrate
```

## Development

Start the development server using:

```
pipenv run python manage.py runserver
```

## VS Code

The yap-backend.code-workspace has predefined settings to help using black and pylint with VSCode. It's recommended to use this workspace and set your pythonPath at folder level settings (wich will be ignored by git).

## Guides

- [Django static files on Heroku](https://devcenter.heroku.com/articles/django-assets#collectstatic-during-builds)
