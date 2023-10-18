from src.cnnClassifier.utils.logging import log 
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.components.model_evaluation_mlflow import ModelEvaluation


config_manager = ConfigManager() # ConfigManager
config = config_manager.get_log_file_config() # config
log_file = config.running_log # log_file



STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigManager() # ConfigManager class
            get_data_evalusation_config = config_manager.get_data_evalusation_config()
            
            eval_obj = ModelEvaluation(config=get_data_evalusation_config)
            eval_obj.evaluation()
            # eval_obj.log_into_mlflow()

        except Exception as ex:
            raise ex



if __name__ == '__main__':
    try:
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
    except Exception as ex:
        log(file_object=log_file, log_message=f"error {ex}")