import os
import sys

import numpy as np
import pandas as pd
import dill

from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        logging.info("Entered evaluate models.")
        
        for i, (model_name, model) in enumerate(models.items()):
            try:
                logging.info(f"Training {model_name}...")
                model.fit(X_train, y_train)  # Train model
                logging.info(f"Model {model_name} trained successfully.")
                
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
                
                train_model_score = r2_score(y_train, y_train_pred)
                test_model_score = r2_score(y_test, y_test_pred)
                
                report[model_name] = test_model_score
                
                logging.info(f"{model_name} - Train Score: {train_model_score}, Test Score: {test_model_score}")
                
            except Exception as ex:
                logging.error(f"Error in model {model_name}: {ex}")
                # You can also raise or handle exceptions here based on your requirement
        
        logging.info("Exiting evaluate models.")
        return report
    
    except Exception as e:
        raise CustomException(e, sys)

    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)