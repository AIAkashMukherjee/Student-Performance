from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


obj=DataIngestion()
train_data,test_data=obj.initate_data_ingestion()   

data_transformation=DataTransformation()
train_arr,test_arr,_=data_transformation.initate_data_transformation(train_data,test_data)

model_trainer_obj=ModelTrainer()
print(model_trainer_obj.initate_model_training(train_arr,test_arr))