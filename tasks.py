from celery import Celery
from flask import Flask, jsonify
import json
import os

flask = Flask(__name__)
app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@flask.route('/jsoncount', methods=['GET'])
#def jsoncount():
#    result = pronounCount.delay()
#    while not result.ready():
#        pass 
#    return result.get()

#@app.task
def pronounCount():
    data = []
    count = 0
    for filename in os.listdir('data'):
        if count < 25:
            with open ('data/'+ filename, 'r') as f:
                count += 1
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



if __name__ == '__main__':
    
    flask.run(host='0.0.0.0',debug=True)
