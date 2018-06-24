from flask import Flask
from task import make_celery

def initialize_app_configuration():

    # Initialize flask application 
    app = Flask(__name__)

    # Add celery server backend on top of redis
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379',
        CELERY_RESULT_BACKEND='redis://localhost:6379'
    )

    return app

flask_app = initialize_app_configuration()
celery = make_celery(flask_app)
