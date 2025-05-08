from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
@app.route('/')

def home():
    day_of_week = datetime.today().strftime('%A')

    return render_template('index.html', day_of_week=day_of_week)
@app.route('/about')
def about():
    return 'Hi This page is *About Us*'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    