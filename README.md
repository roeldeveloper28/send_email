# send_mail

Flask & Celery Asynchronous Emailing

## Features:

1. Send email and process in the background.
2. Get the list of all email state submitted in the first API call. _(See usage below)_

## Setup

1. To install dependencies:
   
   - `$ pipenv install` This will create and start virtual environment.

2. Add .env file to the root folder and provide the following variables:

        DEFAULT_EMAIL=test@example.com
        SG_USERNAME=your_sendgrid_username
        SG_PASSWORD=your_sendgrid_password

        REDIS_URL=redis://localhost:6379
        REDIS_BROKER=redis://localhost:6379
        REDIS_BACKEND=redis://localhost:6379
        REDIS_HOST=localhost
        REDIS_PORT=6379

    > Warning: Do not commit this file.

3.  To start the flask application **MAKE SURE ARE INSIDE AN ACTIVE VIRTUALENV**

    - `$ cd src && python app.py`

4. To start the celery worker

    - `$ cd src`
    - `$ celery -A helpers.celery worker --loglevel=info`

## API

1. `/api/send-email`

    - required params:

      - `email` - Target email address or recipient.
      - `subject` - Subject of the email message.
      - `body` - Body/message of the email.

      
      Return: dict object `{ msg: 'done sending email!' }`

      Error type: `RuntimeError('Something went wrong while sending email message.')`

2. `/api/emails`

    Return: List of dict.


## Usage

1. `$ curl http://127.0.0.1:5000/api/emails`

    OUTPUT

        [
            {
                "email": "test1@example.com",
                "state": "SENT"
            },
            {
                "email": "test2@example.com",
                "state": "FAILED"
            },
            {
                "email": "test2@example.com",
                "state": "PENDING"
            }
        ]


2. `curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/api/send-email -d '{"email": "test1@example.com", "subject": "Hello from flask!", "body": "This is a test email message"}'`

    OUTPUT

        {"msg": "done sending email!"}


