# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# run with IDLE  for testing as VScode runs flask app server in terminal
import requests
res = requests.post('http://localhost:5000/api/addSensorData/1234', json={ "IOTSensorLocation" : "13111111", "Measurement" : "Temperature", "Value": "21.6" })
if res.ok:
    print(res.json())
