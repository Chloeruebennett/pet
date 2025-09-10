import cv2
import numpy as np

def check_qr_in_image(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(img)
    if points is not None:
        print(f"QR-код обнаружен: {data}")
        return True
    else:
        print("QR-код не обнаружен.")
        return False

if __name__ == "__main__":
    result_path = "output_test.jpg"
    check_qr_in_image(result_path)
