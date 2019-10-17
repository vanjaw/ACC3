from celery import Celery
from flask import Flask, jsonify
import json

appFlask = Flask(__name__)

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@appFlask.route('/jsoncount', methods=['GET'])
def js():
    data = []
    with open ('6e72a55b-6b6a-4958-9128-a54f58df58eb', 'r') as f:
        for line in f:
            if line not in ['\n', '\r\n']:
                data.append(json.loads(line))
    hencount = 0
    hancount = 0
    honcount = 0
    dencount = 0
    detcount = 0
    dennecount = 0
    dennacount = 0
    count = 0

    for obj in data:
        if obj["retweeted"] == False:
            text = obj["text"]
            text = text.lower()
            hencount += text.count("hen")
            hancount += text.count("han")
            honcount += text.count("hon")
            dencount += text.count("den")
            detcount += text.count("det")
            dennecount += text.count("denne")
            dennacount += text.count("denna")
            count += 1

    return("{\"han\": " + str(hancount) +
           ", \"hon\": " + str(honcount) +
           ", \"hen\": " + str(hencount) +
           ", \"den\": " + str(dencount) +
           ", \"det\": " + str(detcount) +
           ", \"denne\": " + str(dennecount) +
           ", \"denna\": " + str(dennacount) +
           ", \"nrOfTweets\":"  + str(count) + "}")
    return 4 

@app.task
def add(x, y):
    return x + y

#@app.task
#def readJSON():
#    with open('json.txt') as json_file:
#    	data = json.load(json_file)
#    	return data['id']

if __name__ == '__main__':
    
    appFlask.run(host='0.0.0.0',debug=True)
