from pathlib import Path
from src.cnnClassifier.utils.logging import log
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig
import tensorflow as tf



class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    def get_base_model(self):
        try:
            log_file = self.config.log_file # get the log file path
            
            # get the model:
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape = self.config.params_image_size,
                weights = self.config.params_weights,
                include_top = self.config.params_include_top
            )

            self.save_model(path=self.config.base_model_path, model=self.model)
            log(file_object=log_file, log_message=f"save the model into {self.config.base_model_path}") # logs

        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex



    def _prepare_full_model(self, model, classes, freeze_all, freeze_till, learning_rate):
        try:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"preparing the base model") # logs

            if freeze_all:
                for layer in model.layers:
                    model.trainable = False
            elif (freeze_till is not None) and (freeze_till > 0):
                for layer in model.layers[:-freeze_till]:
                    model.trainable = False
            
            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in)

            full_model = tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction
            )

            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )

            full_model.summary()
            return full_model

        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex


    def update_base_model(self):
        try:
            log_file = self.config.log_file # get the log file path

            self.updated_model = self._prepare_full_model(
                model = self.model,
                classes = self.config.params_classes,
                freeze_all=True,
                freeze_till=None,
                learning_rate=self.config.params_leraning_rate
            )
            log(file_object=log_file, log_message=f"update the base model") # logs

            self.save_model(path=self.config.updated_base_model_path, model=self.updated_model)
            log(file_object=log_file, log_message=f"save the updated model into {self.config.updated_base_model_path}") # logs

        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex


    def save_model(self, path: Path, model: tf.keras.Model):
        try:
            model.save(path)
        except Exception as ex:
            log_file = self.config.log_file # get the log file path
            log(file_object=log_file, log_message=f"error will be: {ex}") # logs
            raise ex



if __name__ == "__main__":
    pass