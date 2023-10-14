from src.cnnClassifier.utils.logging import log 
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.components.model_training import ModelTraining


config_manager = ConfigManager() # ConfigManager
config = config_manager.get_log_file_config() # config
log_file = config.running_log # log_file



STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigManager() # ConfigManager class
            model_training_config = config_manager.get_model_training_config()
            
            train_obj = ModelTraining(config=model_training_config)
            train_obj.get_update_model()
            train_obj.train_valid_generator()
            train_obj.train()          

        except Exception as ex:
            raise ex



if __name__ == '__main__':
    try:
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
        obj = ModelTrainingPipeline()
        obj.main()
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
    except Exception as ex:
        log(file_object=log_file, log_message=f"error {ex}")
        raise ex

