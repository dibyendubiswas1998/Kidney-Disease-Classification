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
