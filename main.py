from src.CancerPrediction import  logger
from src.CancerPrediction.pipeline.stages_01_data_ingestion import DataIngestionTrainingPipeline
from src.CancerPrediction.pipeline.stages_02_data_validation import DataValidationTrainingPipeline
# from src.CancerPrediction.pipeline.stages_03_data_transformation import DataTransformationTrainingPipeline
# from src.CancerPrediction.pipeline.stages_04_model_trainer import ModelTrainerPipeline
# from src.CancerPrediction.pipeline.stages_05_model_evaluation import ModelEvaluationPipeline




STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
