from flask import Flask


app = Flask(__name__)                   # flask application server

# application routing
@app.route("/hello")                         # controller routing to method handler
def hello():

    return "<html><body>Hello</body></html>"     # view - (data display template)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)   # port 80 used already