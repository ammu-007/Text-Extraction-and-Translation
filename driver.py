#%%
import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt

from translator import Translator
from speech import Speech

#%%
imPath = r"E:\Watson NLP\Test\1.jpg" #Path of target image.

pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract' 
#pytesseract executable path

#%%
#Image processing using OpenCV 
image = cv2.imread(imPath, cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh_inv = cv2.threshold(gray_image, 100, 255,cv2.THRESH_BINARY_INV)
plt.imshow(thresh_inv,cmap='gray')
image = cv2.imread(imPath)
d = pytesseract.image_to_data(thresh_inv, output_type=Output.DICT)
text = pytesseract.image_to_string(thresh_inv, lang = 'eng')
print(text)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
n_boxes = len(d['level'])

#Bounding boxes around the text in image
for i in range(n_boxes):
  (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
  img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
plt.imshow(img)

# %%
#Creating object of translator class and passing extracted text to it
translator = Translator(text)

#%%
print(translator.language_list()) #List of supported languages
lang = 'hindi'

# %%
translator.display(lang) #displaying text with specified language

# %%
speech = Speech(text) #Converting text data to speech data
speech.text_to_speech()
