from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.utils.logging import log 
from src.cnnClassifier.pipeline.data_ingestion import DataIntegrationTrainingPipeline
from src.cnnClassifier.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.model_evaluation import ModelEvaluationTrainingPipeline


config_manager = ConfigManager() # ConfigManager
config = config_manager.get_log_file_config() # config
log_file = config.running_log # log_file


STAGE_NAME = "Data Integration Stage"
try:
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
    obj = DataIntegrationTrainingPipeline()
    obj.main()
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
except Exception as ex:
    log(file_object=log_file, log_message=f"error {ex}")





STAGE_NAME = "Prepare Base Model Stage"
try:
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
except Exception as ex:
    log(file_object=log_file, log_message=f"error {ex}")





STAGE_NAME = "Model Training Stage"
try:
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
    obj = ModelTrainingPipeline()
    obj.main()
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
except Exception as ex:
    log(file_object=log_file, log_message=f"error {ex}")




STAGE_NAME = "Model Evaluation Stage"
try:
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
except Exception as ex:
    log(file_object=log_file, log_message=f"error {ex}")