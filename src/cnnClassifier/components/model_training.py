from pathlib import Path
from src.cnnClassifier.utils.logging import log
from src.cnnClassifier.entity.config_entity import ModelTrainingConfig
import tensorflow as tf


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    
    def get_update_model(self):
        try:
            log_file = self.config.log_file # get the log file path
            self.model = tf.keras.models.load_model(
                self.config.updated_base_model_path
            )
            log(file_object=log_file, log_message=f"load the updated model: {self.config.updated_base_model_path}") # logs

        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex
    

    def train_valid_generator(self):
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

            if self.config.params_is_augmentation:
                train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2,
                    **datagenerator_kwargs
                )
            else:
                train_datagenerator = valid_datagenerator

            self.train_generator = train_datagenerator.flow_from_directory(
                directory=self.config.training_data,
                subset="training",
                shuffle=True,
                **dataflow_kwargs
            )
            log(file_object=log_file, log_message=f"generate training and validation data") # logs
        
        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex
    

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
    

    def train(self):
        try:
            log_file = self.config.log_file # get the log file path
        
            self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
            self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

            self.model.fit(
                self.train_generator,
                epochs=self.config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.valid_generator
            )

            self.save_model(
                path=self.config.training_model_path,
                model=self.model
            )
            log(file_object=log_file, log_message=f"after training save the model: {self.config.training_model_path}") # logs


        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex


if __name__ == "__main__":
    pass       