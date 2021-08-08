# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# c:>cd c:\Program Files\Python36\
# python -m pip install flask
# run flask app in terminal to start flask app server
# run test code in IDLE


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/addSensorData/<uuid>', methods=['GET', 'POST'])
def addSensorData(uuid):
    content = request.json
    # check uuid - if uuid in ....
    #contentStr='{ "IOTSensorLocation" : "13111111", "Measurement" : "Temperature", "Value": "21.6" }'
    print("{0} {1} {2} {3}".format(content['IOTSensorLocation'],content['Measurement'],content['Value'],uuid))
    #json_data_response['code'],json_data_response['message'],json_data_response['Measurement'],json_data_response['Setpoint'],json_data_response['Deadband']
    responseData = {'code':'200', 'message' :'OK', 'Measurement': 'Temperature', 'Setpoint' : 22 , 'Deadband' : 1.5}
    return jsonify(responseData)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)