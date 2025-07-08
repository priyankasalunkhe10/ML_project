from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('flight_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = {
            'airline': request.form['airline'],
            'source': request.form['source'],
            'destination': request.form['destination'],
            'date': request.form['journey_date'],
            'stops': request.form['stops'],
            'dep_time': request.form['dep_time'],
            'arr_time': request.form['arr_time'],
            'duration': request.form['duration']
        }
        price = model.predict()
        
        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
