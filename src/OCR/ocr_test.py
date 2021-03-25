import ocr_google
import gcloudCredential

gcloudCredential.credential()
ocr_google.detect_text("./card_image/test4.JPG")