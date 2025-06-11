import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import joblib
import sys
import os

# === Load fine-tuned model and label map ===
MODEL_PATH = "model/t2c_classifier_finetuned.h5"
LABEL_MAP_PATH = "model/label_map.pkl"

model = tf.keras.models.load_model(MODEL_PATH)
class_names = joblib.load(LABEL_MAP_PATH)

# === Input image path from command-line ===
if len(sys.argv) < 2:
    print("Usage: python identify.py <path_to_image>")
    sys.exit()

img_path = sys.argv[1]

if not os.path.exists(img_path):
    print(f"Error: File '{img_path}' does not exist.")
    sys.exit()

# === Image preprocessing ===
IMG_SIZE = (224, 224)

img = image.load_img(img_path, target_size=IMG_SIZE)
img_array = image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # shape (1, 224, 224, 3)
img_array = img_array / 255.0  # normalize like in training

# === Prediction ===
predictions = model.predict(img_array)
predicted_index = np.argmax(predictions[0])
predicted_label = class_names[predicted_index]
confidence = predictions[0][predicted_index]

# === Output ===
print(f"Prediction: {predicted_label} ({confidence*100:.2f}% confidence)")
