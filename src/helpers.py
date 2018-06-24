from config import celery

@celery.task()
def send_mail(emails, body):

    for email in emails:
        print(email)

    return 'successful'
