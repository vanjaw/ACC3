from celery import Celery
from flask import Flask, jsonify
import json

appFlask = Flask(__name__)

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@appFlask.route('/test', methods=['GET'])
def a():
    return 4 

#@app.task
#def add(x, y):
#    return x + y

#@app.task
#def readJSON():
#    with open('json.txt') as json_file:
#    	data = json.load(json_file)
#    	return data['id']

if __name__ == '__main__':
    
    appFlask.run(host='0.0.0.0',debug=True)
