# Reddit-to-Instagram-Repost

Hi, I am a new developer and this is my first repositary on github
I have tried to avoid as many as possible problems, Hope you like it!

This script will do the following
1. Download images from a given subreddit
2. Store Title, Username and downloaded image path in a JSON file
3. Upload each of possible photo to instagram simultaneosly (optional)
   Default caption format - title + Posted by- username + Hashtags


Please provide the following configuration settings:

chromedriver_path = "chromedriver.exe"  #Provide the path for your chromedriver exe

workspace_path = "whatever\file\path\images "  #Provide path to an empty folder to use as workspace, it should not end with '\'


subreddit = 'r/SaimanSays/top'  # Enter your desired subreddit here

numberOfPosts = 500 #Amount to posts to download (Note: Not all the images may be uploaded to Instagram due to unsupported ratio - Success rate is 70% )

upload_to_instagram = True

instagram_username = 'username' 

password = 'password'
