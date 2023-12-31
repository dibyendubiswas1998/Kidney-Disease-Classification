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


    def prepare_base_model_config(self) -> PrepareBaseModelConfig:
        try:
            prepare_base_model_config = PrepareBaseModelConfig(
                log_file = self.config.logs.log_file,
                model_dir =self.config.prepare_base_model.model_dir,
                base_model_path = self.config.prepare_base_model.base_model_path,
                updated_base_model_path =self.config.prepare_base_model.updated_base_model_path,
                params_image_size = self.params.model_params.IMAGE_SIZE,
                params_include_top = self.params.model_params.INCLUDE_TOP,
                params_weights = self.params.model_params.WEIGHTS,
                params_leraning_rate = self.params.model_params.LEARNING_RATE,
                params_classes = self.params.model_params.CLASSES,
            )
            return prepare_base_model_config

        except Exception as ex:
                raise ex
    

    def get_model_training_config(self) -> ModelTrainingConfig:
        try:
            model_training_config = ModelTrainingConfig(
                log_file = self.config.logs.log_file,
                updated_base_model_path = self.config.prepare_base_model.updated_base_model_path,
                training_model_path = self.config.training.trained_model_path,
                training_data = self.config.artifacts.data.data_dir,
                params_epochs = self.params.model_params.EPOCHS,
                params_batch_size = self.params.model_params.BATCH_SIZE,
                params_is_augmentation = self.params.model_params.AUGMENTATION,
                params_image_size = self.params.model_params.IMAGE_SIZE,
            )
            return model_training_config

        except Exception as ex:
            raise ex


    def get_data_evalusation_config(self) -> ModelEvaluationConfig:
        try:
            eval_config = ModelEvaluationConfig(
                log_file = self.config.logs.log_file,
                model_path = self.config.training.trained_model_path,
                training_data = self.config.artifacts.data.data_dir,
                all_params = self.params.model_params,
                mlflow_uri = self.secrect.mlflow.MLFLOW_TRACKING_URI,
                params_image_size = self.params.model_params.IMAGE_SIZE,
                params_batch_size = self.params.model_params.BATCH_SIZE,
                model_performance_report_file_path = self.config.artifacts.model_performance_report.file_path,
            )
            return eval_config

        except Exception as ex:
            raise ex


if __name__ == '__main__':
    cf = ConfigManager()
    print(cf.get_model_training_config())
    
