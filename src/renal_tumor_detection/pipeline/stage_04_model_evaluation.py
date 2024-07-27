from renal_tumor_detection.config.configuration import ConfigurationManager
from renal_tumor_detection.components.model_evaluation_mlflow import Evaluation
from renal_tumor_detection import logger
import os


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:           
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            
            logger.info("Starting evaluation.")
            evaluation.evaluation()
            logger.info("Evaluation completed.")
            
            logger.info("Saving score.")
            evaluation.save_score()
            logger.info("Score saved.")
            
            # logger.info("Logging into MLflow.")
            # evaluation.log_into_mlflow()
            # logger.info("Logged into MLflow.")


        except Exception as e:
            logger.exception(e)
            raise e



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            