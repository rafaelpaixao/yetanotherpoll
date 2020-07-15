# Instalation

1. Install [Python 3](https://www.python.org/)

1. Install [Pipenv](https://github.com/pypa/pipenv)

   ```
   pip install pyenv
   ```

1. Use pipenv to generate an enviroment with this project dependencies:

   ```
   pipenv install
   ```

1. Let's start the Django development server just to make sure:

   ```
   pipenv run server
   ```

This command should start Django's development server with some warnings about the migrations that need to be applied.

1. Stop the server with ctrl+C (or kill the terminal).

1. Now, if you wish, you can use Postgres by setting a enviroment variable like:

   ```
   DATABASE_URL=postgres://user:password@host:port/dbname
   ```

   With pipenv, this is simple as [creating a .env file](https://pipenv.pypa.io/en/latest/advanced/#automatic-loading-of-env).

   Or you can roll out with SQLite by skiping this step.

1. Let's create some tables:

   ```
   pipenv run python manage.py migrate
   ```

1. And a super user:

   ```
   pipenv run python manage.py createsuperuser
   ```

1. Now, start the dev server again
