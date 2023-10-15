from pathlib import Path
from src.cnnClassifier.utils.logging import log
from src.cnnClassifier.utils.common_utils import save_report
from src.cnnClassifier.entity.config_entity import ModelEvaluationConfig
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
import os



class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
    
    def valid_generator(self):
        try:
            log_file = self.config.log_file # get the log file path

            datagenerator_kwargs = dict(
                rescale = 1./255,
                validation_split=0.20
            )

            dataflow_kwargs = dict(
                target_size=self.config.params_image_size[:-1],
                batch_size=self.config.params_batch_size,
                interpolation="bilinear"
            )

            valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )

            self.valid_generator = valid_datagenerator.flow_from_directory(
                directory=self.config.training_data,
                subset="validation",
                shuffle=False,
                **dataflow_kwargs
            )
            log(file_object=log_file, log_message=f"generate validation data") # logs
        
        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex
    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        try:
            log_file = self.config.log_file # get the log file path
            self.model = self.load_model(self.config.model_path)
            self.valid_generator()
            self.score = self.model.evaluate(self.valid_generator)
            self.save_score()
            log(file_object=log_file, log_message=f"evaluate and save the score") # logs

        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex
    

    def save_score(self):
        try:
            scores = {"loss": self.score[0], "accuracy": self.score[1]}
            save_report(file_path=Path(self.config.model_performance_report_file_path), report=scores)

        except Exception as ex:
            raise ex 
        

    def log_into_mlflow(self):
        try:
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            
            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metrics(
                    {"loss": self.score[0], "accuracy": self.score[1]}
                )
                # Model registry does not work with file store
                if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
                else:
                    mlflow.keras.log_model(self.model, "model")
        
        except Exception as ex:
            raise ex
        


if __name__ == "__main__":
    pass 