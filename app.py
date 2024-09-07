from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import os


app=Flask(__name__)


data_path = r'./data/cleaned_data.csv'
model_path = r'./models/LRModel.pkl'

df=pd.read_csv(data_path)
pipe_lr=pickle.load(open(model_path,'rb'))

@app.route('/')
def index():
    locations=sorted(df['location'].unique())
    return render_template('index.html',locations=locations)


@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    location = data['location']
    total_sqft = float(data['total_sqft'])
    bath = int(data['bath'])
    bhk = int(data['bhk'])
    
    input=pd.DataFrame([[location,total_sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    predicted_price = pipe_lr.predict(input)[0]
    
    return jsonify(predicted_price=round(predicted_price,3))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)

