import os
from src.cnnClassifier.utils.common_utils import read_params
from src.cnnClassifier.constants import *
from src.cnnClassifier.entity.config_entity import *



class ConfigManager:
    def __init__(self, secrect_file_path=SECRET_FILE_PATH, config_file_path=CONFIG_FILE_PATH, 
                 params_file_path=PARAMS_FILE_PATH):
                
        self.secrect = read_params(secrect_file_path) # read information from config/secrect.yaml file
        self.config = read_params(config_file_path) # read information from config/config.yaml file
        self.params = read_params(params_file_path) # read information from params.yaml file
    

    def get_log_file_config(self) -> LogConfig:
        try:
            log_file = LogConfig(running_log = self.config.logs.log_file)
            return log_file
        
        except Exception as ex:
            raise ex


    def get_data_ingestion_config(self):
        try:
            data_ingestion_config = DataIngestionConfig(
                s3_service_name = self.secrect.s3_access_details.service_name,
                s3_region_name = self.secrect.s3_access_details.region,
                s3_aws_access_key_id = self.secrect.s3_access_details.access_key,
                s3_aws_secret_access_key = self.secrect.s3_access_details.secret_key,
                s3_bucket_name = self.secrect.data_info.bucket_name,
                s3_normal_folder_prefix = self.secrect.data_info.normal_folder_prefix,
                s3_tumor_folder_prefix = self.secrect.data_info.tumor_folder_prefix,
                normal_local_directory = self.config.artifacts.data.normal_dir,
                tumor_local_directory = self.config.artifacts.data.tumor_dir,
                log_file = self.config.logs.log_file,
                num_records_extract = self.secrect.num_records_extract
            )
            return data_ingestion_config
            
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    cf = ConfigManager()
    print(cf.get_log_file_config())
    
