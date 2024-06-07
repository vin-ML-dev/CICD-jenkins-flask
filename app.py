from flask import Flask,jsonify,request
import os
import pickle
import numpy as np


app = Flask(__name__)

@app.route("/")
def hello():
   return "Welcome to CICD Jenkins Flask demo app !"

@app.route("/predict",methods=["POST"])
def predict():

   test_data = request.json['data']
   #print(test_data,type(test_data))

   test_data = np.array([test_data])

   ##load model
   with open('trained_model/model.pkl', 'rb') as f:
        model = pickle.load(f)

   pred = model.predict(test_data)

   if pred[0]==0:
      resp = {'prediction':'Setosa'}
   elif pred[0]==1:
      resp = {'prediction':'Versicolor'}
   elif pred[0]==2:
      resp = {'prediction':'Virginica'}
      
   return jsonify(resp)
   
   
if __name__ == "__main__":
   #port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=5000)
