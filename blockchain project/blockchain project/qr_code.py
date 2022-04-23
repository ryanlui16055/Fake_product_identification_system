from cgitb import grey
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import imutils

def qr_code_decoder(img_path):
    img = cv2.imread(img_path)
    grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    decode_img = pyzbar.decode(grey_img)     
    for text in decode_img:
        print(text)

        (x, y, w, h) = text.rect
        draw_rectangle(x,y,w,h,img)

        if text !=[]: return text.data.decode("utf-8")
        else: return 'Cannot decode image'

def draw_rectangle(x,y,w,h,img):
    
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    cv2.imshow("Image", img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# for testing photo recognizebitily, feel free to change angle to test.        
def rotate_img(img_path):
    img = cv2.imread(img_path)
    rotated_img = imutils.rotate_bound(img,angle=30)
    cv2.imshow("hah",rotated_img)
    cv2.waitKey(0)

print(qr_code_decoder(r'.\barcode2.PNG'))
rotate_img(r'.\barcode2.PNG')
