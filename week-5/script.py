import pickle

with open('week-5/dv.bin', 'rb')  as f:
    dv = pickle.load(f)

with open('week-5/model1.bin', 'rb') as f:
    model = pickle.load(f)

client = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform(client)

y_pred = model.predict_proba(X)[0,1]

print(y_pred)