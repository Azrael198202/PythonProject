from OCR.ocr_google import detect_text
from OCR.gcloudCredential import credential
import getCurrency

from exchangeratesapi import Api

#credential()
#detect_text("./src/card_image/test4.JPG")

#out_value = getCurrency.convert_currency("JPY","CNY",1000)

#print("JPY to CNY {}".format(out_value))
api = Api()
print(api.get_rate('JPY', 'CNY',start_date="2021-03-01", end_date="2021-03-25"))
#print(api.get_rate('CNY', 'JPY'))
