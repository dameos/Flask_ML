import cv2
import numpy as np
from sklearn.externals import joblib

def transform_data(image):
    sift = cv2.xfeatures2d.SIFT_create()
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, descs = sift.detectAndCompute(gray, None)
    kmeans = joblib.load('models/kmeans.pkl')
    centers = kmeans.cluster_centers_
    hist = np.zeros(len(centers))
    for feature in descs:
        prediction = kmeans.predict([feature])
        hist[prediction] = 1 + hist[prediction]
    return hist
