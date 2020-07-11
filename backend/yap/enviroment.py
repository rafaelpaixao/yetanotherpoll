import os

# Consts
ENV_DEV = "DEVELOPMENT"
ENV_HEROKU = "HEROKU"

# Variable used in settings
ENVIROMENT = os.getenv("DJANGO_ENVIROMENT", ENV_DEV)
