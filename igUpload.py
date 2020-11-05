import tempfile
import PIL
import numpy as np
from instabot import Bot
import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps

class ig:

    def __init__(self, username, password, watermark_text, watermark):
        self.username = username
        self.password = password
        self.watermark_text = watermark_text
        self.watermark = watermark
        self.bot = Bot()
        self.bot.login(username=username, password=password)


    def upload(self, title, photo, un):
        # Customize your caption here----------------------------------------
        content = str(title) + "\n\nPosted by: " + un + "\n\nFollow: @"+str(self.username) + " for more \n\n#davie504 #davie504bass #davie504memes #bassmemes #musicmemes #bassist #guitarmemes #bassistmemes"
        # -------------------------------------------------------------------
        try:
            self.prepare_and_fix_photo(photo=photo)
            self.bot.upload_photo(photo=photo, caption=content)
        except Exception as e:
            print("     Could not upload to Instagram! ", e)

    def prepare_and_fix_photo(self, photo):

        im = Image.open(photo)
        width, height = im.size

        draw = ImageDraw.Draw(im)

        if self.watermark:
            text = str(self.watermark_text)

            font = ImageFont.truetype('arial.ttf', 30)
            textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

        # draw watermark in the bottom right corner
        # thin border
            fillcolor = "white"
            shadowcolor = "black"

            draw.text((x - 3, y), text, font=font, fill=shadowcolor)
            draw.text((x + 3, y), text, font=font, fill=shadowcolor)
            draw.text((x, y - 3), text, font=font, fill=shadowcolor)
            draw.text((x, y + 3), text, font=font, fill=shadowcolor)

        # thicker border
            draw.text((x - 3, y - 3), text, font=font, fill=shadowcolor)
            draw.text((x + 3, y - 3), text, font=font, fill=shadowcolor)
            draw.text((x - 3, y + 3), text, font=font, fill=shadowcolor)
            draw.text((x + 3, y + 3), text, font=font, fill=shadowcolor)

        # now draw the text over it
            draw.text((x, y), text, font=font, fill=fillcolor)
            print("     Watermark Added!")
            im.save(photo)

        color = "white"

        print("     W:"+str(width)+" H:"+str(height))
        ratio = width / height
        print("     R:"+str(ratio))
        if ratio < 0.8:
            required_width = height * 0.85 - width
            side = math.ceil(required_width / 2)
            border = (side, 0, side, 0)
            new_img = ImageOps.expand(im, border=border, fill=color)
            print("     White border was added to fix image ratio.")
            new_img.save(str(photo))
        elif ratio > 1.91:
            required_height = width / 1.19 - height
            side = math.ceil(required_height / 2)
            border = (0, side, 0, side)
            new_img = ImageOps.expand(im, border=border, fill=color)
            print("     White border was added to fix image ratio.")
            new_img.convert("RGB")
            new_img.save(photo)

