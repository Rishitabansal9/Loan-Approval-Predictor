import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(  self,
        income: int,
        existingLoans: int,
        loanAmount: int,
        loanTenure: int,
        occupation: str
        ):

        self.income = income
        self.existingLoans = existingLoans
        self.loanAmount = loanAmount
        self.loanTenure = loanTenure
        self.occupation = occupation


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Income": [self.income],
                "Number of Existing Loans": [self.existingLoans],
                "Loan Amount": [self.loanAmount],
                "Loan Tenure": [self.loanTenure],
                "Occupation": [self.occupation]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
