from flask import Flask, render_template

import requests
import json
import datetime

app = Flask(__name__)                   # flask application server

#SG sensor interface functions
def getTempemperatureFromSensor():
    return(21.1)
def getHumidtyFromSensor():
    return(45.9)
def getLightlevelFromSensor():
    return(1036)

# application routing
@app.route("/")                         # controller routing to method handler
def measurements():

    title = "Measured IOT Sensor data"
    localDateTime = datetime.datetime.now()     # current date , time
    measuredTemperature = getTempemperatureFromSensor()
    measuredHumidity = getHumidtyFromSensor()
    measuredlightlevel = getLightlevelFromSensor()

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