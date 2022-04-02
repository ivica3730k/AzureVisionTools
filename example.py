import cv2

from AzureVisionTools import AzureObjectDetectionEngine as ObjectDetection

if __name__ == "__main__":
    ENDPOINT = ""
    SUBSCRIPTION_KEY = ""
    ObjectDetection.load_credentials(endpoint=ENDPOINT, subscription_key=SUBSCRIPTION_KEY)
    image = cv2.imread("testimage1.jpg")
    print(ObjectDetection.inference_from_cv2_image(image))
    print(ObjectDetection.inference_from_file("testimage1.jpg"))
    ObjectDetection.inference_from_cv2_image_and_draw(image)
    ObjectDetection.inference_from_file_and_draw("testimage1.jpg")
