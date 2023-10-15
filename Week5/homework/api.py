import pickle
from flask import Flask
from flask import request
from flask import jsonify

dict_file = 'dv.bin'
model_file = 'model2.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dict_file, 'rb') as f_in:
    dv = pickle.load(f_in)
    
app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    
    return jsonify(y_pred)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)