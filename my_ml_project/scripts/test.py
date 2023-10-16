from sklearn.metrics import classification_report, confusion_matrix

y_true = train_generator.classes
y_pred_probs = model_2.predict(train_generator)
y_pred = np.round(y_pred_probs)

print("Classification Report:\n", classification_report(y_true, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))