import os
from pathlib import Path

from flask import Flask
from flask_mail import Mail, Message
from redis import Redis

from dotenv import load_dotenv
from task import make_celery


env_path = Path('..') / '.env'
load_dotenv(dotenv_path=str(env_path))


def app_setting():

    # Initialize flask application
    app = Flask(__name__)

    # Add celery server backend on top of redis
    app.config.update(
        CELERY_BROKER_URL=str(os.getenv('REDIS_BROKER')),
        CELERY_RESULT_BACKEND=str(os.getenv('REDIS_BACKEND')),
    )

    # Add SendGrid configuration API
    app.config.update(
        MAIL_SERVER='smtp.sendgrid.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME=os.getenv('SG_USERNAME'),
        MAIL_PASSWORD=os.getenv('SG_PASSWORD'),
        MAIL_DEFAULT_SENDER=os.getenv('DEFAULT_MAIL'),
    )

    return app


flask_app = app_setting()
redis_db = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), charset='utf-8', decode_responses=True)
celery = make_celery(flask_app)
mail = Mail(flask_app)
