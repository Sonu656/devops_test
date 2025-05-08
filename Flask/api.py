from flask import Flask, request, render_template

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sonu:1234@cluster0.t0mtdcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

    
api = Flask(__name__)

@api.route('/')
def home():
    return render_template('index.html')

@api.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    print(form_data)

    return form_data

if __name__ == '__main__':

    api.run(debug=True)



