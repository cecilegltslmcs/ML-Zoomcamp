import pickle

dict_file = 'dv.bin'
model_file = 'model1.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dict_file, 'rb') as f_in:
    dv = pickle.load(f_in)

customer = {
    "job": "retired",
    "duration": 445,
    "poutcome": "success"
}

def predict(customer):
    X = dv.transform(customer)
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred

y_pred = predict(customer)
print(y_pred)