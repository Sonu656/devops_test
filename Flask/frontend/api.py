from flask import Flask, render_template, request
import requests

BACKEND_URL = 'http://0.0.0.0:9000'

api = Flask(__name__)

@api.route('/')
def home():
    return render_template('index.html')

@api.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)

    return 'Data Submitted Successfully'

if __name__ == '__main__':

    api.run(host='0.0.0.0',port=8000, debug=True)



