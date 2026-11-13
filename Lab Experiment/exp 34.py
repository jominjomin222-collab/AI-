
# Image Classification using Neural Network

import tensorflow as tf

# Load dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build neural network
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(x_train, y_train, epochs=3)

# Test model
loss, accuracy = model.evaluate(x_test, y_test)

print("Accuracy:", accuracy)

# Predict image
prediction = model.predict(x_test[:1])

print("Predicted Digit:", prediction[0].argmax())
print("Actual Digit:", y_test[0])
