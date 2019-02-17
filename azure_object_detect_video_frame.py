"""
Sends numpy frame by frame video feed to output annotated numpy frame with classification and rectangles
"""

import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


class AzureObjDetect:
    def __init__(self):
        self.subscription_key = "cc0261b3b4534ecabca75b855c0b0516"
        self.vision_base_url = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/analyze"
        self.headers = {'Ocp-Apim-Subscription-Key': self.subscription_key, 'Content-Type': 'application/octet-stream'}
        self.params = {'visualFeatures': 'Categories,Tags,Description,Faces,Color'}
        self.image_data = None
        self.analysis = None
        self.image = None
        self.image_caption = None

    def analyze_frame(self, np_array):
        self.image_data = np_array.tobytes()
        response = requests.post(self.vision_base_url, headers=self.headers, params=self.params, data=self.image_data)
        response.raise_for_status()
        self.analysis = response.json()
        print(self.analysis)
        self.image_caption = self.analysis["description"]["captions"][0]["text"].capitalize()

    def show_annotated_image(self):
        image = Image.open(BytesIO(self.image_data))
        plt.imshow(image)
        plt.axis("off")
        _ = plt.title(self.image_caption, size="x-large", y=-0.1)
        plt.show()

    # def annotate_frame(self):



if __name__ == "__main__":
    import cv2

    im_np_array = cv2.imread("C:/Users/barne/Downloads/family.jpg")

    obj_detect = AzureObjDetect()
    obj_detect.analyze_frame(im_np_array)
    #obj_detect.show_annotated_image()
