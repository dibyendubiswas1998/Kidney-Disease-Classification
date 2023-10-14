from src.cnnClassifier.utils.logging import log 
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel


config_manager = ConfigManager() # ConfigManager
config = config_manager.get_log_file_config() # config
log_file = config.running_log # log_file



STAGE_NAME = "Prepare Base Model Stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigManager() # ConfigManager class
            get_prepare_base_model_config = config_manager.prepare_base_model_config()
            
            base_model_obj = PrepareBaseModel(config=get_prepare_base_model_config)
            base_model_obj.get_base_model()
            base_model_obj.update_base_model()

        except Exception as ex:
            raise ex



if __name__ == '__main__':
    try:
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
    except Exception as ex:
        log(file_object=log_file, log_message=f"error {ex}")