from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import json
import os.path
from os import path
import re



class redditPost:

    promoted = '/div/div/div[2]/div[1]/div/div[1]/span[1]'
    img = "/div/div/div[2]/div[3]/div/div[2]/a/div/div/img"
    comment = "/div/div/div[2]/div[4]/div[2]/a/span"
    heading = '/div/div/div[2]/div[2]/div[1]/a/div/h3'
    username = "/div/div/div[2]/div[1]/div/div[1]/div/a"
    workspace = os.getcwd() + "\images"


    def __init__(self, driver, position):
        redditPost.driver = driver
        redditPost.i = position

    def isPromoted(self):
        xpath = '//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div[' + str(self.i) + ']'
        post = self.driver.find_element_by_xpath(xpath + self.promoted)
        if post.text == "PROMOTED":
            return True
        else:
            return False

    def getHeading(self):
        xpath = '//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div[' + str(self.i) + ']'
        h = self.driver.find_element_by_xpath(xpath + self.heading)
        return h.text

    def getUser(self):
        xpath = '//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div[' + str(self.i) + ']'
        u = self.driver.find_element_by_xpath(xpath + self.username)
        return u.text

    def isImage(self):
        xpath = '//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div[' + str(self.i) + ']'
        try:
         
            self.driver.find_element_by_xpath(xpath + self.img)
            
        except NoSuchElementException:
            return False
        return True

    def isValid(self):
        xpath = '//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div[' + str(self.i) + ']'
        element = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(10)
        
        if self.isPromoted() :
            print(">Post is promoted")
            return False
        elif not self.isImage():
            print(">Post does't contain an image")
            return False
        else:
            return True

    def downloadImage(self, title):


        xpath = '//*[@class="rpBJOHq2PR60pnwJlUyP0"]/div[' + str(self.i) + ']'
        img = '/html/body/img'
        element = self.driver.find_element_by_xpath(xpath + self.img)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        clean_title = " ".join(re.split("[^a-zA-Z]*", title))
        clean_title = clean_title.replace(" ", "")

        self.file_path = self.workspace+'\%s.jpg' % (clean_title)

        try:
            print('     Downloading...')
            self.driver.find_element_by_xpath(xpath + self.img).click()
            time.sleep(3)
            image = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[5]/a')
            time.sleep(5)
            url = image.get_attribute('href')
            try:
                if not os.path.isfile(self.file_path+'.REMOVE_ME'):
                    urllib.request.urlretrieve(url, self.file_path)
                    print('     Sucessfully saved image to: ', self.file_path)
                    self.saveInfo()
                else:
                    print('     Post has already been downloaded one time')
                    return False
            except Exception as e:
                print('     Error saving the file! ')
                print(e)
            time.sleep(3)
            self.driver.execute_script("window.history.go(-1)")



        except NoSuchElementException:
            print('     Failed to download image!')
        return True

    def writeToJSONFile(self, dir, fileName, data):

        filePathNameWExt =  dir + '/' + fileName + '.json'
        if not os.path.isfile(filePathNameWExt):
            print('     Creating JSON file...')
            with open(filePathNameWExt, 'w+') as fp:
                json.dump(data, fp, indent=4)
            print('     Info stored at: ' + filePathNameWExt)

        else:
            with open(filePathNameWExt, 'a+') as fp:
                json.dump(data, fp, indent=4)
            print('     Info stored at: ' + filePathNameWExt)



    def saveInfo(self):

        info = {
            "title" : self.getHeading(),
            "user" : self.getUser(),
            "location" : self.file_path,
            "uploaded" : False
        }
        self.writeToJSONFile(self.workspace, 'ri', info)
