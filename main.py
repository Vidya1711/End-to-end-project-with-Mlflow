from mlProject import logger
from mlProject.pipeline.data_ingestion import DataIngestionTrainingPipeline

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