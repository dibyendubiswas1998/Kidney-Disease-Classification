from pathlib import Path
from dataclasses import dataclass
import os



@dataclass(frozen=True)
class LogConfig:
  running_log: Path


@dataclass(frozen=True)
class DataIngestionConfig:
  s3_service_name: str
  s3_region_name: str
  s3_aws_access_key_id: str
  s3_aws_secret_access_key: str
  s3_bucket_name: str
  s3_normal_folder_prefix: str
  s3_tumor_folder_prefix: str
  normal_local_directory: Path
  tumor_local_directory: Path
  log_file: Path
  num_records_extract: int


@dataclass(frozen=True)
class PrepareBaseModelConfig:
  log_file: Path
  model_dir: Path
  base_model_path: Path
  updated_base_model_path: Path
  params_image_size: list
  params_include_top: bool
  params_weights: str
  params_leraning_rate: int 
  params_classes: int


@dataclass(frozen=True)
class ModelTrainingConfig:
  log_file: Path
  updated_base_model_path: Path
  training_model_path: Path
  training_data: Path
  params_epochs: int
  params_batch_size: int
  params_is_augmentation: bool
  params_image_size: list


@dataclass(frozen=True)
class ModelEvaluationConfig:
  log_file: Path
  model_path: Path
  training_data: Path
  all_params: dict
  mlflow_uri: str
  params_image_size: list
  params_batch_size: int
  model_performance_report_file_path: Path

