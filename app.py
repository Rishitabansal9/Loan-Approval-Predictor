from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from flask import jsonify

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.logger import logging

application=Flask(__name__,static_folder='static')
app=application

## Route for home page

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        data = CustomData(
            income=request.form.get('income'),
            existingLoans=request.form.get('existingLoans'),
            loanAmount=request.form.get('loanAmount'),
            loanTenure=request.form.get('loanTenure'),
            occupation=request.form.get('occupation')
        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Return the result as JSON
        return jsonify({'prediction_result': results[0]})

    # If it's a GET request, return the template
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
