# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
import requests
res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"lalala"})
if res.ok:
    print(res.json())
