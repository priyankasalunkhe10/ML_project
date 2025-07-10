from flask import Flask, render_template, request, redirect,url_for
import pandas as pd
import pickle
import json
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), 'flight_model.pkl')

model = pickle.load(open(model_path, 'rb'))
with open('feature_order.json', 'r') as f:
    feature_order = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        airline = request.form['airline']
        source = request.form['source']
        destination = request.form['destination']
        stops = int(request.form['stops']) 
        journey_date = pd.to_datetime(request.form['journey_date'])
        booking_date = pd.to_datetime(request.form['booking_date'])

        days_before = (journey_date - booking_date).days
        day = journey_date.day
        month = journey_date.month
        weekday = journey_date.weekday()

        data = {
            'Days_Before_Journey': [days_before],
            'Journey_Day': [day],
            'Journey_Month': [month],
            'Journey_Weekday': [weekday],
            'Total_Stops': [stops]  
        }

        trip = f"{source} - {destination}"

        trip_options = [
            'Delhi-Cochin',     
            'Kolkata-Banglore',    
            'Banglore-Delhi',       
            'Banglore-New Delhi',     
            'Mumbai-Hyderabad',      
            'Chennai-Kolkata'  
        ]  

        for t in trip_options:
            data[f"Trip_{t}"] = [1 if trip == t else 0]



        Airlines = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet']
        for a in Airlines:
            data[f"Airline_{a}"] = [1 if airline == a else 0]


        final_input = pd.DataFrame(data)
        final_input = final_input.reindex(columns=feature_order)
        price = model.predict(final_input)[0]
        
        return render_template('result.html',
                               prediction=price,
                               airline=airline,
                               source=source,
                               destination=destination,
                               journey_date=journey_date.date(),
                               booking_date=booking_date.date(),
                               stops=stops)
    else:
        return redirect(url_for('home')) 
if __name__ == '__main__':
    app.run(debug=True)
