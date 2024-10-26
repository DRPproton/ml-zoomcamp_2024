import pickle

from flask import Flask
from flask import request
from flask import jsonify

app = Flask('churn')

app.route('', methods=['GET'])
def main():
    return 'pong'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)