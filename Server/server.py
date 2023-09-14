from flask import Flask, Response

app = Flask(__name__)


@app.route('/ping')
def ping():
    return Response("{'a':'b'}", status=200, mimetype='application/json')
    
if __name__ == "__main__":
   app.run(debug=True, port=10000)