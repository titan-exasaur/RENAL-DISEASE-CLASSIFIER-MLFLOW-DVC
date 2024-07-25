from renal_tumor_detection import logger
from renal_tumor_detection.config.configuration import ConfigurationManager
from renal_tumor_detection.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare base model stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        #prepare_base_model.save_model

if __name__ == '__main__':
    try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> {STAGE_NAME} completed! <<<<<<<<<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e