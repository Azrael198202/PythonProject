from OCR.ocr_google import detect_text
from OCR.gcloudCredential import credential

credential()
detect_text("./src/card_image/test4.JPG")