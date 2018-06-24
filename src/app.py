from flask import Response, json, jsonify, request, url_for

from config import flask_app, redis_db
from helpers import send_mail as sendmail

app = flask_app

@app.route('/')
def index():
    return 'Index page'

@app.route('/api/emails')
def emails():
    return 'List of emails'

@app.route('/api/send-email', methods=['POST'])
def send_email():

    try:
        
        data = request.get_json()
        sendmail.delay(data['emails'], data['body'])
        
        return  Response(json.dumps({ 'msg': 'done sending email!' }), status=200, mimetype='application/json')

    except Exception as e:
        return  Response(e, status=500, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
