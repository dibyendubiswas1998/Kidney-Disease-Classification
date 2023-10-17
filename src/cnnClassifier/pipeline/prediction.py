import numpy as np
import tensorflow as tf
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename

    
    def predict(self):
        try:
            model = tf.keras.models.load_model("artifacts/model/training_model.h5")
            imagename = self.filename
            test_image = tf.keras.preprocessing.image.load_img(imagename, target_size = (224,224))
            test_image = tf.keras.preprocessing.image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)

            result = np.argmax(model.predict(test_image), axis=1)
            print(result)

            if result[0] == 1:
                prediction = 'Tumor'
                return [{ "image" : prediction}]
            else:
                prediction = 'Normal'
                return [{ "image" : prediction}]

        except Exception as ex:
            raise ex



if __name__ == '__main__':
    pp = PredictionPipeline("img.jpg")
    pp.predict()
    
