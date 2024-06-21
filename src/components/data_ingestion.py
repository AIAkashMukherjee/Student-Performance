import os,sys
from src.logger.custom_logging import logger
from src.exceptions.expection import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class variable

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

@dataclass # no need for __init__
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts/data_ingestion',"train.csv")
    test_data_path: str=os.path.join('artifacts/data_ingestion',"test.csv")
    raw_data_path: str=os.path.join('artifacts/data_ingestion',"data.csv")

class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()

    def initate_data_ingestion(self):
        logger.info('Entered in Data ingestion')
        try:
            df=pd.read_csv('/Users/akashmukherjee/Programming/Practise ML/Students Performance/data/stud (1).csv')

            os.makedirs(os.path.dirname(os.path.join(self.data_ingestion_config.raw_data_path)),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            logger.info('Train test split done data ingestion')

            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logger.info("Ingestion of the data is completed")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)    
        

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initate_data_ingestion()   

    # data_transformation=DataTransformation()
    # train_arr,test_arr,_=data_transformation.initate_data_transformation(train_data,test_data)

    # model_trainer_obj=ModelTrainer()
    # print(model_trainer_obj.initate_model_training(train_arr,test_arr))

