from config import Message, celery, mail


@celery.task()
def send_mail(email, subject, body):

    try:
        msg = Message(
            subject=subject, 
            sender='test@example.com',
            recipients=[email],
        )
        msg.body = body

        mail.send(msg)

    except Exception:
        raise RuntimeError('Something went wrong while sending email message.')


    
