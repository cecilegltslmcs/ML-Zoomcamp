import tensorflow as tf
from tensorflow as keras

model = keras.models.load_model('./clothing-model.h5')
tf.saved_model.save(model, 'clothing-model')