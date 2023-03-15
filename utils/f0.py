from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://shop.flipperzero.one/"

options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run the browser in headless mode
driver = webdriver.Chrome(options=options)

def get_page(url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(text(),"Flipper Zero is a portable multi-tool for pen-testers and geeks in a toy-like body")]'), "Flipper Zero is a portable multi-tool for pen-testers and geeks in a toy-like body"))
    html_content = driver.page_source
    return html_content

def check_in_stock(html_content):
    #print(html_content)
    if html_content.find('<button type="submit" name="add" aria-disabled="true" aria-label="Sold out" class="btn product-form__cart-submit" aria-haspopup="dialog" data-add-to-cart="">') != -1:
        print("Out of stock")
    else:
        print("In stock")

url_page = get_page(url)
check_in_stock(url_page)


driver.quit()

