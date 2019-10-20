
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot= webdriver.Firefox()
    def login(self):
        bot=self.bot
        bot.get("https://twitter.com/")
        time.sleep(2)
        email= bot.find_element_by_class_name("email-input")
        password= bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    def like_tweet(self,hashtag):
        bot=self.bot
        bot.get("https://twitter.com/search?q=" +  hashtag +"&src=typeahead_click")
        time.sleep(4)
        for i in range(1,5):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            tweets = bot.find_elements_by_class_name("css-1dbjc4n r-18u37iz r-thb0q2")
           






##data-testid="tweet"