import cv2
import numpy as np

def detect(model, image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (150, 150))
    img = np.array(img).reshape(-1, 150, 150, 1)
    img = img / 255.
    img = np.array(img)

    pred = model.predict([ img ])
    return 1 if pred[0][0]>0.5 else 0