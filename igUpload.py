from instabot import Bot
import os

class ig:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = Bot()
        self.bot.login(username=username, password=password)


    def upload(self, title, photo, un):
        print("     Starting to Upload on Instagram")
        self.bot.upload_story_photo(photo=photo, upload_id=None)

        # Customize your caption here----------------------------------------
        content = str(title) + "\n\nPosted by: " + un + "\n\nFollow: @"+str(self.username) + " for more #davie504memes #davie504 #bassmemes #bassist #bassistmemes"
        # -------------------------------------------------------------------
        try:

            self.bot.upload_photo(photo=photo, caption=content)
        except Exception as e:
            print("     Could not upload to Instagram! ", e)
