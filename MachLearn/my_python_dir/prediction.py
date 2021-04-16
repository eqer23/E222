##this is where i will make a prediciton using my pkl file
from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model

my_model = load("heartfailure.pkl")


#endpoint points here
def my_prediction(id):
    dummy = np.array(id)
    dummyT = dummy.reshape(1,-1)
    prediction = my_model.predict(dummyT)
    #name = class_names[prediction]
   # name = name.tolist()
   # name_str = json.dumps(name)
   # string = [t_str, r_str, name_str]
    return str(prediction[0])


