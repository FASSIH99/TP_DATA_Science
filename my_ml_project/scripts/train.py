model_2= Sequential([
    Conv2D(32,(3,3), activation='relu',input_shape=(128,128,1)),
    MaxPooling2D((2,2)),
    Conv2D(64,(3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])
model_2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


history = model_2.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator,
    #callbacks=[custom_callback]
)