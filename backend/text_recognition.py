import os, io
from google.cloud import vision
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from pdf2image import convert_from_path
import cv2
import PyPDF2

def convertArraytoBytes(array):
    success, encoded_image = cv2.imencode('.png', array)
    return encoded_image.tobytes()

def get_text_from_pdf(pdf_path: str) -> str:
    doc = open(pdf_path, 'rb')
    readpdf = PyPDF2.PdfFileReader(doc)
    totalpages = readpdf.numPages

    client = vision.ImageAnnotatorClient()

    if os.name == 'nt':
        pages = convert_from_path(pdf_path, 150, poppler_path=r"C:\Program Files (x86)\poppler-0.68.0\bin")
    else:
        pages = convert_from_path(pdf_path, 150)

    page_no=0
    j=0
    
    # console_file = open("dump.txt", "a")
    for page in pages:

        page_no = page_no+1

        if(page_no < 3):
            continue
        
        if(page_no >= totalpages-1):
            break
        # console_file.write('hello ' + str(i))
        print(page_no)

        # page.save('page'+str(i)+'.jpg', 'JPEG')
        image = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

        # image = cv2.imread('page'+str(i)+'.jpg')
        original = image.copy()
        headerImage = original[160:300,0:3000]
        # save headerImage
        headerImageBytes = convertArraytoBytes(headerImage)
        headerRequestImage = vision.Image(content=headerImageBytes)
        headerImageResponse = client.text_detection(image=headerRequestImage)
        #split after :
        headerText = headerImageResponse.text_annotations[0].description.split(":")[1]
        headerText = headerText.lstrip()


        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        thresh = cv2.threshold(blurred, 150,255,cv2.THRESH_BINARY_INV)[1]

        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        image_number = 0
        min_area = 3000


        for c in cnts:
            area = cv2.contourArea(c)
            if area > min_area:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(original, (x, y), (x+ w, y+ h), (36,255,12), 2)

                img_list = []

                if(h < 157):

                    row1 = original[y:y+h, x:x+379]
                    row2 = original[y:y+h, x+380:x+756]
                    row3 = original[y:y+h, x+757:x+1133]
                    for i in range(3):
                        img_list.append(convertArraytoBytes(array=eval('row'+str(i+1))))

                else:
                    row1 = original[y:y+157, x:x+379]
                    row2 = original[y:y+157, x+380:x+756]
                    row3 = original[y:y+157, x+757:x+1133]
                    row4 = original[y+157:y+h, x:x+379]
                    row5 = original[y+157:y+h, x+380:x+756]
                    row6 = original[y+157:y+h, x+757:x+1133]

                    for i in range(6):
                        img_list.append(convertArraytoBytes(array=eval('row'+str(i+1))))

                
                for content in img_list:
                    image = vision.Image(content=content)

                    response = client.text_detection(image=image)
                    df = pd.DataFrame(columns=['locale', 'description'])

                    texts = response.text_annotations
                    for text in texts:
                        text.description = text.description + "\n" + "address: " + headerText
                        df = df.append(
                            dict(
                                locale=text.locale,
                                description=text.description
                            ),
                            ignore_index=True
                        )

                    out_file = open("temp/locale-out.txt", "a")
                    try:
                        out_file.write(df['description'][0])
                        out_file.write("\n------------\n")
                    except:
                        pass
                    out_file.close()

                j = j+1
    # console_file.close()
if __name__ == "__main__":
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'
    get_text_from_pdf("temp/test.pdf")
