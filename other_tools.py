import random
import json
import segno
import base64
import os.path
from PIL import Image, ImageDraw, ImageFont


empty_id = "000000000000"

def generate_id():
    return str(random.randint(100000000000, 999999999999))

def validate_id(identifier):
    if len(identifier) == 12:
        try:
            int(identifier)
            return True
        except:
            return False
    return False

def get_users_in_queue(queue):
    print(queue)
    user_ids = [e['user_id'] for e in queue]
    return user_ids

def make_queue_qr_image(queue_id):
    def generate_qr(data, filename):
        qrcode = segno.make_qr(str(data))
        qrcode.save(str(filename)+".png")
        return str(filename)+".png"

    image_path = str(queue_id)+".png"
    if not os.path.exists(image_path):
        qr_path = generate_qr(queue_id, queue_id)
        image = Image.open(image_path)
        image = image.resize((200, 200))
        font = ImageFont.truetype("arial.ttf", 20)
        drawer = ImageDraw.Draw(image)
        drawer.text((35, 175), str(queue_id), font=font, fill='black')

        image.save(image_path)

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string