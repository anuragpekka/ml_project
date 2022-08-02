from housing.constant import *
from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.component.data_validation import DataValidation
from housing.component.data_ingestion import DataIngestion

configs = Configuration()
''''
validation_config = configs.get_data_validation_config()
print(f"validation_config: {validation_config}")
'''
transformation_config = configs.get_data_transformation_config()
print(f"transformation_config: {transformation_config}")

'''pipe = Pipeline()
pipe.run_pipeline()'''
