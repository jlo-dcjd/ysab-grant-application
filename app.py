from flask import Flask, request, render_template, jsonify
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")

app = Flask(__name__)

cluster = MongoClient(mongo_uri)
db = cluster[db_name]
collection = db['ysab']

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
        try:     
            # Get form data
            form_data = request.form.to_dict()
            name = request.form.get('name')
            email = request.form.get('email')

            # Insert data into MongoDB
            collection.insert_one(form_data)

            # return jsonify({'success': True, 'message': 'Form data submitted successfully'})
            return render_template('confirmation.html', name=name, email=email)
        except Exception as e:
            # return jsonify({'success': False, 'error': str(e)})
             return render_template('error.html', error=str(e))

# post = {'_id': 0, "name": "tim", "score":5}
# collection.insert_one(post)\

if __name__ == '__main__':
    app.run()
