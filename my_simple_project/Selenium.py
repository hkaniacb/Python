from selenium import webdriver
import time
driver = webdriver.Chrome()

def delayForBrowser(self, delay=3000):
    time.sleep(delay/1000.00)
driver.get("https://translate.google.pl/?hl=pl")


text_to_transalte = "dom"

text_box_translator = driver.find_element_by_id("source")
text_box_translator.clear()
text_box_translator.send_keys(text_to_transalte)
time.sleep(4)
text_box_translator = driver.find_element_by_class_name("tlid-translation translation")
print(text_box_translator.get_attribute("innerText"))
time.sleep(3)
print(text_box_translator.text)



