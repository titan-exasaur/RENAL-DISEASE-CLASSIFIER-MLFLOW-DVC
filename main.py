from dotenv import load_dotenv
from renal_tumor_detection import logger
from renal_tumor_detection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from renal_tumor_detection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from renal_tumor_detection.pipeline.stage_03_model_training import ModelTrainingPipeline
from renal_tumor_detection.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"******************************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation stage"
try:
#    os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/tinytachyon14341/RENAL-DISEASE-CLASSIFIER-MLFLOW-DVC.mlflow"
#    os.environ["MLFLOW_TRACKING_USERNAME"] = "tinytachyon14341"
#    os.environ["MLFLOW_TRACKING_PASSWORD"] = "f7f82fe5075a413434f0e5cd779d34f62dd5fd9d"
    load_dotenv()
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

