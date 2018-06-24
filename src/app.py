from flask import json, url_for, request, Response
from config import flask_app

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

        send_res = sendmail.delay(data['emails'], data['body'])
        send_res.get()

        if send_res.failed():
            return  Response(json.dumps({ 'msg': 'Sending email failed!' }), status=400, mimetype='application/json')
        
        return  Response(json.dumps({ 'msg': 'Email successfully sent!' }), status=200, mimetype='application/json')

    except Exception as e:
        return  Response(e, status=500, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
