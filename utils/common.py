import os
import random
from io import BytesIO
from PIL import Image

from django.conf import settings
from django.core.files.base import ContentFile


def get_background_folder():
    path = os.path.join(settings.MEDIA_ROOT, 'background')
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def get_background_image():
    root_path = get_background_folder()
    name_list = [n for n in os.listdir(root_path) if os.path.splitext(n)[1].upper() in ('.JPG', 'JPEG', '.PNG')]
    if name_list:
        return os.path.join(root_path, random.choice(name_list))
    else:
        return None


def set_background_image(src):
    if not os.path.exists(src):
        return None
    img_src = Image.open(src).convert("RGBA")
    path_bg = get_background_image()
    if not path_bg or not os.path.exists(path_bg):
        return None
    img_bg = Image.open(path_bg)
    img_bg = fit_background_size(img_bg, img_src).convert("RGBA")
    c = Image.new('RGBA', img_bg.size, (255, 255, 255, 0))
    position = get_background_position(img_bg.size, img_src.size)
    c.paste(img_src, position, img_src)

    result = Image.alpha_composite(img_bg, c)

    buffer = BytesIO()
    result.save(fp=buffer, format='PNG')
    return ContentFile(buffer.getvalue())


def fit_background_size(img_bg, img_src):
    # bg_width, bg_height = img_bg.size
    src_width, src_height = img_src.size
    new_width = src_width / 0.8
    new_height = src_height / 0.8
    img_bg = img_bg.resize((int(new_width), int(new_height)))
    return img_bg


def get_background_position(bg_size, src_size):
    bg_width, bg_height = bg_size
    src_width, src_height = src_size
    return int((bg_width - src_width) / 2), int((bg_height - src_height) / 2)
