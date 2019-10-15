from celery import Celery
import json

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

@app.task
def js():
    with open('json.txt') as json_file:
    	data = json.load(json_file)
    	return data['id']
