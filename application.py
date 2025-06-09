import pandas as pd
from flask import Flask
from flask import render_template,request
import pandas as pd
import pickle
import numpy as np

model=pickle.load(open("Cleaned_car.pickle","rb"))
app=Flask(__name__)
car=pd.read_csv("Cleaned car.csv")
@app.route('/',methods=['GET','POST'])
def index():
    companies=sorted(car["company"].unique())
    car_models=sorted(car["name"].unique())
    year=sorted(car["year"].unique(),reverse=True)
    fuel_type=car["fuel_type"].unique()

    companies.insert(0,"Select Company")

    return render_template("index.html",companies=companies,car_models=car_models,years=year,fuel_type=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get("company")
    car_model=request.form.get("car_model")
    year=request.form.get("year")
    fuel_type=request.form.get("fuel_type")
    kms_driven=request.form.get("kilo_driven")

    prediction=model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],
                                          columns=["name","company","year","kms_driven","fuel_type"]))

    print(prediction)
    return str(np.round(prediction[0],2))
if __name__=="__main__":
    app.run(debug=True)
