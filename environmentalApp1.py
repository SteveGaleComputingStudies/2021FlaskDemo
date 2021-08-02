from flask import Flask, render_template

import requests
import json
import datetime

app = Flask(__name__)                   # flask application server


@app.route("/")                         # controller routing to method handler
def measurements():

    title = "Measured data"
    localDateTime = datetime.datetime.now()     # current date , time
    measuredTemperature = 21.2
    measuredHumidity = 45.9
    measuredlightlevel = 1036

# model (data format)

    templateData = {
        'title' : title,
        'time': localDateTime,
        'temperature' : measuredTemperature,
        'humidity' : measuredHumidity,
        'lightLevel' : measuredlightlevel
        }
    return render_template('main.html', **templateData)     # view - (data display template)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)   # port 80 used already