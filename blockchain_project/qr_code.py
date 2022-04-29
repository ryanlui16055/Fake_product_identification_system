import cv2
import pyzbar.pyzbar as pyzbar
import qrcode
import os
from tkinter import messagebox
import base64

# decode QR code image
def qr_code_decoder(img_path):
    img = cv2.imread(img_path)
    decode_img = pyzbar.decode(img)

    for text in decode_img:

        if text != []:
            return base64.b64decode(text.data)
        else:
            return False


# txt is qr code content, string type and it will save as image, feel free to change name in img.save("")
def generate_QRcode(txt):
    txt = base64.b64encode(txt)
    img = qrcode.make(txt)
    img.save(r"blockchain_project\blockchain_project\images\product_qr_code.jpg")
    image = cv2.imread(
        r"blockchain_project\blockchain_project\images\product_qr_code.jpg"
    )
    cv2.imshow("Image", image)
    messagebox.showinfo(
        "System",
        "File download" + "\nFile path:" + os.path.abspath("product_qr_code.jpg"),
    )
    cv2.waitKey(0)


def identify_hash(provided_chain, chain_in_product):
    for x, y, z in zip(provided_chain, chain_in_product, range(len(provided_chain))):
        if x["previous_hash"] != y["previous_hash"]:
            return False
        if z == len(provided_chain):
            break
    return True
