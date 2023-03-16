from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def get_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Run the browser in headless mode
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(text(),"Flipper Zero is a portable multi-tool for pen-testers and geeks in a toy-like body")]'), "Flipper Zero is a portable multi-tool for pen-testers and geeks in a toy-like body"))
    html_content = driver.page_source
    driver.quit()
    return html_content

def check_in_stock(html_content):
    #print(html_content)
    if html_content.find('<button type="submit" name="add" aria-disabled="true" aria-label="Sold out" class="btn product-form__cart-submit" aria-haspopup="dialog" data-add-to-cart="">') != -1:
        return False
    else:
        return True

def create_message(target,link):

    regex = re.compile(r"https?://(?:[^./]+\.)?([^./]+)\.[^.]+\.?.*")
    match = regex.match(link)
    vendor = match.group(1)

    message = """From: PY Locator <python.testhere@gmail.com>
To: To {} <{}>
Subject: Flipper zero in stock at {}

Hello {},

There are some Flipper zero in stock at {},

you can check them out here : 

{}

Have a good day !
""".format(target["name"],target["email"],vendor,target["name"],vendor,link)
    return message


