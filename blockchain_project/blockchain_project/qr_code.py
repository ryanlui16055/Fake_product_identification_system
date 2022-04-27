from cgitb import grey
import cv2
from matplotlib import image
import numpy as np
import pyzbar.pyzbar as pyzbar
import imutils
import qrcode
from PIL import Image
import json


def qr_code_decoder(img_path):
    img = cv2.imread(img_path)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decode_img = pyzbar.decode(grey_img)
    for text in decode_img:
        print(text)

        (x, y, w, h) = text.rect
        draw_rectangle(x, y, w, h, img)

        if text != []:
            return text.data.decode("utf-8")
        else:
            return "Cannot decode image"


def draw_rectangle(x, y, w, h, img):

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# for testing photo recognizebitily, feel free to change angle to test.
def rotate_img(img_path):
    img = cv2.imread(img_path)
    rotated_img = imutils.rotate_bound(img, angle=30)
    cv2.imshow("hah", rotated_img)
    cv2.waitKey(0)


# txt is qr code content, string type and it will save as image, feel free to change name in img.save("")
def generate_QRcode(txt):
    img = qrcode.make(txt)
    img.save(r"blockchain_project\blockchain_project\images\test.jpg")
    image = cv2.imread(r"blockchain_project\blockchain_project\images\test.jpg")
    cv2.imshow("Image", image)
    cv2.waitKey(0)


def identify_hash(provided_chain, chain_in_product):
    for x, y, z in zip(provided_chain, chain_in_product, range(len(provided_chain))):
        if x["previous_hash"] != y["previous_hash"]:
            return False
        if z == len(provided_chain):
            break
    return True


# print(qr_code_decoder(r".\test.png"))
# rotate_img(r".\abc.png")
# cv2.imshow("QR", generate_QRcode("this is me"))
# generate_QRcode("this is me")
