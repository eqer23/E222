##this is where i will make a prediciton using my pkl file
from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model

my_model = load("heartfailure.pkl")

#endpoint points here
def my_prediction(id):
    return


