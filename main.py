import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from redditPost import *
from igUpload import *
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Preferences-------------------------------------------------------------------------

subreddit = 'r/Davie504/top'  # Enter your desired subreddit here
numberOfPosts = 500  # Amount to posts to download
upload_to_instagram = True
instagram_username = 'r.davie504'
password = 'shreyas@4'

# ------------------------------------------------------------------------------------


cwd = os.getcwd()
if not os.path.isdir(cwd + "/images"):
    print("Making new folder to store images..")
    os.makedirs(cwd + "/images")
    print("Images will be stored in: ", cwd + "/images")

ig.username = instagram_username
ig.password = password

if upload_to_instagram:
    inst = ig(instagram_username, password)


cwd = os.getcwd()
chromedriver_path = cwd + "\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
pref = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", pref)
chrome_options.set_headless(True)
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
driver.maximize_window()

try:

    print("Navigating : " + subreddit)
    driver.get("https://www.reddit.com/" + subreddit)
    time.sleep(5)
    baseURL = driver.current_url
    foundPosts = 0

    print('Starting to find images-')

    for i in range(1, numberOfPosts):

        if baseURL == driver.current_url:
            time.sleep(3)
            p = redditPost(driver, i)
            time.sleep(5)
            try:

                if not p.isValid():
                    print('     Skipping..')
                else:
                    time.sleep(3)
                    foundPosts += 1
                    print(">Found a valid post! --- Total posts: " + str(foundPosts))
                    heading = str(p.getHeading())
                    user = str(p.getUser())
                    print("     Title: " + heading)
                    if p.downloadImage(p.getHeading()):
                        if upload_to_instagram:
                            inst.upload(heading, p.file_path, user)

            except NoSuchElementException:
                print("Searching...")
            except Exception as e:
                print("An error occurred! ", e)
        else:
            driver.back()
            i = i-1

except Exception as e:
    print('Script failed: ', e)
    driver.quit()
