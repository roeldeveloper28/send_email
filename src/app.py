from flask import Response, json, jsonify, request, url_for

from config import flask_app, redis_db
from helpers import send_mail as sendmail

app = flask_app


status_label = {
    'PENDING': 'QUEUED',
    'SUCCESS': 'SENT',
    'FAILURE': 'FAILED'
}

def get_status(celery_state):
    return status_label[celery_state]


@app.route('/')
def index():
    return 'Index page'

@app.route('/api/emails')
def emails():
    tasks = redis_db.hgetall('task')
    status = [{'state': get_status(sendmail.AsyncResult(k).state), 'email': v}  for k, v in tasks.items()]
    return jsonify(status)

@app.route('/api/send-email', methods=['POST'])
def send_email():

    try:
        
        data = request.get_json()
        task = sendmail.apply_async((data['email'], data['subject'], data['body']))

        redis_db.hset('task', task.id, data['email'])
        
        return  Response(json.dumps({ 'msg': 'done sending email!' }), status=200, mimetype='application/json')

    except Exception as e:
        return  Response(e, status=500, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
