from instabot import Bot



class ig:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = Bot()
        self.bot.login(username = username, password = password)

    def upload(self, title, location, un):
        print("     Starting to Upload on Instagram")
        
        #Customize your caption here----------------------------------------
        content = str(title) + "\n\nPosted by: " + un + "\n\nFollow for more\n\n#instagram #reddit"
        #-------------------------------------------------------------------
        try:

            self.bot.upload_photo(location, caption=content, )
        except Exception as e:
            print("     Could not upload to Instagram! ", e)
