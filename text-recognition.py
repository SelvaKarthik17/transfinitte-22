import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import time
import numpy as np

from pdf2image import convert_from_path
import cv2
import PyPDF2

doc = open('pdfName.pdf', 'rb')
readpdf = PyPDF2.PdfFileReader(doc)
totalpages = readpdf.numPages

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

client = vision.ImageAnnotatorClient()

pages = convert_from_path('pdfName.pdf', 500, poppler_path=r"C:\Program Files (x86)\poppler-0.68.0\bin")

i=0
j=0

for page in pages:

    i = i+1

    if(i < 3):
        continue
    
    if(i == totalpages):
        break

    # page.save('page'+str(i)+'.jpg', 'JPEG')
    image = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

    # image = cv2.imread('page'+str(i)+'.jpg')
    original = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blurred, 230,255,cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    image_number = 0
    min_area = 8000

    def convertArraytoBytes(array):
        success, encoded_image = cv2.imencode('.png', array)
        return encoded_image.tobytes()

    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(original, (x, y), (x+ w, y+ h), (36,255,12), 2)

            img_list = []

            if(h < 500):

                row1 = original[y:y+h, x:x+1225]
                row2 = original[y:y+h, x+1250:x+2475]
                row3 = original[y:y+h, x+2500:x+3750]
                for i in range(3):
                    img_list.append(convertArraytoBytes(array=eval('row'+str(i+1))))

            else:
                row1 = original[y:y+500, x:x+1225]
                row2 = original[y:y+500, x+1250:x+2475]
                row3 = original[y:y+500, x+2500:x+3750]
                row4 = original[y+500:y+h, x:x+1225]
                row5 = original[y+500:y+h, x+1250:x+2475]
                row6 = original[y+500:y+h, x+2500:x+3750]

                for i in range(6):
                    img_list.append(convertArraytoBytes(array=eval('row'+str(i+1))))

            
            for content in img_list:
                image = vision.Image(content=content)

                response = client.text_detection(image=image)
                df = pd.DataFrame(columns=['locale', 'description'])

                texts = response.text_annotations
                for text in texts:
                    df = df.append(
                        dict(
                            locale=text.locale,
                            description=text.description
                        ),
                        ignore_index=True
                    )

                out_file = open("tamil-out.txt", "a")
                out_file.write(df['description'][0])
                out_file.write("\n------------\n")
                out_file.close()

            j = j+1

