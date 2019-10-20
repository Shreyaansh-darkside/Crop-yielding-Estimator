import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    poly_reg = PolynomialFeatures(degree =2 ,interaction_only=False, include_bias=True)
    prediction = model.predict(poly_reg.fit_transform(final_features))

    output = round(prediction[0], 2)
    gdd_day = round(890.4/output, 2)


    return render_template('index.html', prediction_text='The no. of days remaining to be yield : {}'.format(gdd_day))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    gdd_day = round(890.4/output, 2)
    return jsonify(gdd_day)

if __name__ == "__main__":
    app.run(debug=True)
