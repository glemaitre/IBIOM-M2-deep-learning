from tensorflow.keras.utils import to_categorical

n_classes = np.unique(y_train).size
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)
