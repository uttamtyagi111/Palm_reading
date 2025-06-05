import cv2
import numpy as np

def preprocess_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges

def extract_features(edges):
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)
    features = []
    if lines is not None:
        for line in lines[:10]:  # limit features
            x1, y1, x2, y2 = line[0]
            angle = np.arctan2(y2 - y1, x2 - x1)
            length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            features.extend([angle, length])
    while len(features) < 20:
        features.append(0)
    return features
