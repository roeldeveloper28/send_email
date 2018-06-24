from config import Message, celery, mail, redis_db


@celery.task()
def send_mail(emails, body):

    try:
        msg = Message(
            'Hello from Flask!', 
            sender='test@example.com',
            recipients=[email for email in emails],
        )
        msg.body = body

        mail.send(msg)

        for email in emails:
            redis_db.sadd('emails', str(email))

    except Exception:
        raise RuntimeError('Something went wrong while sending email message.')


    
