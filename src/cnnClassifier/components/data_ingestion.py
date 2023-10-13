import os
import boto3
from src.cnnClassifier.utils.logging import log
from src.cnnClassifier.utils.common_utils import clean_prev_dirs_if_exis, create_dir
from src.cnnClassifier.utils.common_utils import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config
        

    def download_data_from_s3_bucket(self):
        try:
            log_file = self.config.log_file # get the log file path
            
            # mention S3 configuration details:
            s3_client = boto3.client(
                            service_name=self.config.s3_service_name,
                            region_name=self.config.s3_region_name,
                            aws_access_key_id=self.config.s3_aws_access_key_id,
                            aws_secret_access_key=self.config.s3_aws_secret_access_key
                        )
            
            """
                start downloading and storing operating for normal image data
            """

            # clean directory if it exists: 
            clean_prev_dirs_if_exis(dir_path=self.config.normal_local_directory) 
            log(file_object=log_file, log_message=f"remove directory if exits: {self.config.normal_local_directory}") # logs
            
            # create directory:
            create_dir(dirs=[self.config.normal_local_directory])
            log(file_object=log_file, log_message=f"create fresh directory for storing the normal image  data in:  {self.config.normal_local_directory}") # logs

            # start downloading the data from S3 bucket: normal images
            log(file_object=log_file, log_message=f"start the downloading operation of normal data, of records: {self.config.num_records_extract}") # logs
            objects_normal = s3_client.list_objects_v2(Bucket=self.config.s3_bucket_name, Prefix=self.config.s3_normal_folder_prefix)
            for key, obj in enumerate(objects_normal.get('Contents', [])):
                if key >=1  and key <= self.config.num_records_extract: # extrcat the paticular number of  records
                    file_key = obj['Key']
                    local_file_path = os.path.join(self.config.normal_local_directory, os.path.basename(file_key))

                    s3_client.download_file(self.config.s3_bucket_name, file_key, f"{local_file_path}")
            
            log(file_object=log_file, log_message=f"successfully downloaded the nomal images into: {self.config.normal_local_directory}") # logs
            

            """
                start downloading and storing operating for tumor image data
            """
            # clean directory if it exists: 
            clean_prev_dirs_if_exis(dir_path=self.config.tumor_local_directory)
            log(file_object=log_file, log_message=f"remove directory if exits: {self.config.tumor_local_directory}") # logs

            # create directory
            create_dir(dirs=[self.config.tumor_local_directory])
            log(file_object=log_file, log_message=f"create fresh directory for storing the tumor image  data in:  {self.config.tumor_local_directory}") # logs

            # start downloading the data from S3 bucket: tumor images
            log(file_object=log_file, log_message=f"start the downloading operation of tumor data, of records: {self.config.num_records_extract}") # logs
            objects_normal = s3_client.list_objects_v2(Bucket=self.config.s3_bucket_name, Prefix=self.config.s3_tumor_folder_prefix)
            for key, obj in enumerate(objects_normal.get('Contents', [])):
                if key >=1  and key <= self.config.num_records_extract: # extrcat the paticular number of  records
                    file_key = obj['Key']
                    local_file_path = os.path.join(self.config.tumor_local_directory, os.path.basename(file_key))

                    s3_client.download_file(self.config.s3_bucket_name, file_key, f"{local_file_path}")
            
            log(file_object=log_file, log_message=f"successfully downloaded the tumor images into: {self.config.tumor_local_directory}") # logs
            

        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex



if __name__ == "__main__":
    pass
