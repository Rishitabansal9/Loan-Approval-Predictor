import os
import sys
import pandas as pd

from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path:str=os.path.join('artifacts',"model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,X_train,X_test,y_train,y_test):
        logging.info("Entered the Model Training method.")
        try:
            models = {
        
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
           
            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            logging.info("Ingestion of the data is completed")

            best_model=models[best_model_name]

            if(best_model_score<0.6):
                raise CustomException("No best model found.")
            
            logging.info("Best found model on both training & testing data")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted=best_model.predict(X_test)

            r2_square=r2_score(y_test,predicted)
            return r2_square
        
        
        except Exception as e:
            raise CustomException(e,sys)


