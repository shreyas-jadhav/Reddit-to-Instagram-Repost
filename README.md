# Reddit-to-Instagram-Repost

## This script will do the following:
* Download images from a given subreddit
* Store Title, Username and downloaded image path in a JSON file
* Process Images to fit expected Ratio and Add Borders + Watermark
* Upload each of images to instagram simultaneosly
   Default caption format - title + Posted by- username + Hashtags
   
  ### Updates and Fixes:
   * Added watermark support.
   * Resizes image automatically to fit ratio.
_________________________________________________________________________

Please provide the following configuration settings:

chromedriver_path = "chromedriver.exe"  #Provide the path for your chromedriver exe

workspace_path = "whatever/file\pat/\images "  #Provide path to an empty folder to use as workspace, it should not end with '/'


subreddit = 'r/SaimanSays/top'  # Enter your desired subreddit here

numberOfPosts = 500 #Amount to posts to download (Note: Not all the images may be uploaded to Instagram due to unsupported ratio - Success rate is 70% )

upload_to_instagram = True

instagram_username = 'username' 

password = 'password'
_________________________________________________________________________

Please do the following before running:
   pip install selenium
   pip install instabot

then Run main.py
