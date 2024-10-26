import pickle

from flask import Flask
from flask import request
from flask import jsonify

app = Flask('churn')

with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)
with open('model1.bin', 'rb') as f:
    model = pickle.load(f)



@app.route('/predict', methods=['POST'])
def main():
    client = request.get_json()
    X = dv.transform(client)
    prediction = model.predict_proba(X)[0,1]

    return jsonify({'Probability Supscription': round(float(prediction), 3)})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)