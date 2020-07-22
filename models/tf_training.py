import tf_preprocessing

if __name__ = '__main__':
    #  reshape to vectors
    train_img = train_img.reshape(60000,-1).astype(np.float32)
    test_img = test_img.reshape(10000,-1).astype(np.float32)

    #  normalize to (0,1)
    train_img, test_img = train_img/255, test_img/255

    #  set up validation data
    validation_img = train_img[:10000]
    validation_labels = train_labels[:10000]

    train_img = train_img[10000:]
    train_labels = train_labels[10000:]

    #  configure the model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(128, input_shape = (784,), activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    #  type
    #  > model.summary()
    #  for a model summary

    #  choosing optimizers
    optimizer = tf.keras.optimizers.SGD()
    loss=tf.keras.losses.SparseCategoricalCrossentropy()
    accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

    model.compile(optimizer=optimizer,
                  loss=loss,
                  metrics=[accuracy])

    #  training the model
    history = model.fit(train_img, train_labels,
                        epochs = 5, 
                        batch_size = 16, 
                        validation_data = (validation_img, validation_labels))

    #  saving the model parameters
    model.save('sequential_nn_save.h5')
