from housing.constant import *
from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline

configs = Configuration()
validation_config = configs.get_data_validation_config()
print(f"validation_config: {validation_config}")

pipe = Pipeline(configs)
pipe.run_pipeline()
