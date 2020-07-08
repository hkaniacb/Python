from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import  random


class InstagramLike():

     def __init__(self,username, password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome()


     def login(self):
         browser=self.driver
         browser.get("https://www.instagram.com/accounts/login/")
         browser.maximize_window()
         input_username=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"Input[name='username']")),"Input username not exist")
         input_username.clear()
         input_username.send_keys(self.username)
         input_password = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"Input[name='password']")),"Input password not exist")
         input_password.clear()
         input_password.send_keys(self.password)
         input_password.send_keys(Keys.ENTER)


     def likephoto(self, tag):
         browser=self.driver
         browser.get("https://www.instagram.com/explore/tags/" + tag + "/")
         hrefImage=[]
         try:
             all_href=WebDriverWait(browser,5).until(EC.presence_of_all_elements_located((By.TAG_NAME,"a")),"Link image")
             all_herfImagetag=[item.get_attribute('href') for item in all_href if "com/p/" in item.get_attribute('href')]
             [ hrefImage.append(item) for item in all_herfImagetag if item not in hrefImage]
         except Exception as e:
             if "Link image" in str(e):
                 print(str(e))
             else:
                 print(str(e))

         print("Count image href: {}".format(len(hrefImage)))
         for link in hrefImage:
             try:
               delay= random.randint(250,2500)
               browser.get(link)
               self.randomDelay(delay)
               print("Go to: {} i czas wygenerowany to {}".format(link,delay))
               button_like=WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,"//span[@aria-label='Lubiê to!']")),"Button lubie to")
               button_like.click()
               self.randomDelay(1000)
             except Exception as e:
               print(str(e))
               continue

     def destroyBrowser(self):
          self.driver.quit()

     def randomDelay(self, delay=3000):
         time.sleep(delay/1000)


user="xxx"
pswd="xxx"
hashtags="""#girls #boys"""
print(hashtags.strip())
lista=[x.strip() for x in hashtags.split("#")]

#tag=random.choice(hashtags.split("#").strip())

try:
    inst = InstagramLike(user, pswd)
    inst.login()
    while True:
         tag=""
         while not tag:
             tag= random.choice(lista)
         print("hastag is: '{}' ".format(tag))
         inst.likephoto(tag)
except TimeoutException as ex:
    print(str(ex))
except Exception as e:
    print("error")
finally:
    pass
    inst.destroyBrowser()
