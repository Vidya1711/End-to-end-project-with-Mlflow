from mlProject import logger
from mlProject.pipeline.data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.model_trainer import ModelTrainerTrainingPipeline


logger.info("Welcome to our customer logging")


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME = "Data Validation Stage"
 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e  




STAGE_NAME = "Data Transformation Stage"
 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e  



STAGE_NAME = "Model Trainer Stage"
 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e  