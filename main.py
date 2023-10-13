from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.utils.logging import log 
from src.cnnClassifier.pipeline.data_ingestion import DataIntegrationTrainingPipeline

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

    