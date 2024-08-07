from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app=Flask(__name__)
df=pd.read_csv(r'C:\Users\harsh\Desktop\House Price Prediction\data\cleaned_data.csv')
pipe_lr=pickle.load(open(r'C:\Users\harsh\Desktop\House Price Prediction\models\LRModel.pkl','rb'))

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
    app.run(debug=True,port=4000)

