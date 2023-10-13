from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.utils.logging import log 


config_manager = ConfigManager() # ConfigManager
config = config_manager.get_log_file_config() # config
log_file = config.running_log # log_file



STAGE_NAME = "Data Integration Stage"


class DataIntegrationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigManager() # ConfigManager class
            get_data_ingestion_config = config_manager.get_data_ingestion_config()
            dd = DataIngestion(config=get_data_ingestion_config)
            dd.download_data_from_s3_bucket()

        except Exception as ex:
            raise ex



if __name__ == '__main__':
    try:
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} started {str('<')*15}")
        obj = DataIntegrationTrainingPipeline()
        obj.main()
        log(file_object=log_file, log_message=f"{str('>')*15} Stage: {STAGE_NAME} completed {str('<')*15} \n\n")
     
    except Exception as ex:
        log(file_object=log_file, log_message=f"error {ex}")

