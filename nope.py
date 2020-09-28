from instapy import InstaPy
import time
from time import sleep
from selenium import webdriver
#import schedule

#login credentials
username = 'Attar_Souk'
password = 'Attar@123i'

session = InstaPy(
                  username=username,
                  password=password,
                  headless_browser=False
                  
                  )

session.login()

#Follow people based on the stated hashtags below
session.follow_by_tags(['perfume'], amount=0)

#Like Post using hashtags given below
session.like_by_tags(['perfume','fragances','attarcollection'], amount=0)

#Unfollow users who don't follow back
session.unfollow_users(amount=10, nonFollowers=True, style="RANDOM", unfollow_after=336*60*60, sleep_delay=655)

#End the bot session
session.end()
