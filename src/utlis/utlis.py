import os,sys
import pickle
import pandas as pd
from src.exceptions.expection import CustomException
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file:
            pickle.dump(obj,file)
    except Exception as e:
        raise CustomException(e,sys)        
    

def evaluate_model(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            param=params[list(models.keys())[i]]

            rs=RandomizedSearchCV(model,param,cv=5,random_state=42,n_jobs=-1)
            rs.fit(X_train,y_train)

            model.set_params(**rs.best_params_)
            model.fit(X_train,y_train)

            y_pred=model.predict(X_test)
            test_model_score=r2_score(y_test,y_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

            
    except Exception as e:
        raise CustomException(e,sys)
  
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)  