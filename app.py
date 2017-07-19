from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions


app = FlaskAPI(__name__)
@app.route("/")
def main_response():
    print('Received http request at main')
    return {'hey': 'u did it'}
@app.route("/test/", methods=['GET', 'POST'])
def test_response():
    if request.method == 'GET':
        return {'status': 'strong'}
    return {'still': 'alive'}

if __name__ == "__main__":
    app.run(debug=True)
