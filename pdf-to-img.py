from pdf2image import convert_from_path
import cv2
import PyPDF2

doc = open('pdfName.pdf', 'rb')
readpdf = PyPDF2.PdfFileReader(doc)
totalpages = readpdf.numPages

pages = convert_from_path('pdfName.pdf', 500)

i=0
j=0

for page in pages:

    i = i+1

    if(i < 3):
        continue
    
    if(i == totalpages):
        break

    page.save('page'+str(i)+'.jpg', 'JPEG')

    image = cv2.imread('page'+str(i)+'.jpg')
    original = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blurred, 230,255,cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    image_number = 0
    min_area = 8000
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
            row = original[y:y+h, x:x+w]
            cv2.imwrite('row_'+str(j)+'.png', row)
            j = j+1
