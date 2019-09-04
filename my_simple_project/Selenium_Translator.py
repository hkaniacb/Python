from selenium import webdriver
import time
import clipboard
import keyboard
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
shortcut = 'alt+x'  # define your hot-key
print('Hotkey set as:', shortcut)


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)


driver = webdriver.Chrome()
driver.get("https://translate.google.pl/#view=home&op=translate&sl=en&tl=pl")
# driver.maximize_window()
driver.minimize_window()


def transalte_my_text():
    # while True:
    # text_to_translate = input("Podaj fraze do przetłumaczenia: ")
    driver.maximize_window()
    text_to_translate = clipboard.paste()
    print(text_to_translate)

    textBox_translator = driver.find_element_by_xpath("//textarea[@id='source']")  # id("source")
    highlight(textBox_translator)

    textBox_translator.send_keys(text_to_translate)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='text-wrap tlid-copy-target']")))


    #$time.sleep(4)
    # textBox_after_translate =  driver.find_element_by_class_name("text-wrap tlid-copy-target")
    textBox_after_translate = driver.find_element_by_xpath("//div[@class='text-wrap tlid-copy-target']")
    highlight(textBox_after_translate)
    print(textBox_after_translate.text)
    driver.minimize_window()
    textBox_translator.clear()

keyboard.add_hotkey(shortcut, transalte_my_text)  # <-- attach the function to hot-key
print("Press ESC to stop.")
keyboard.wait('esc')
