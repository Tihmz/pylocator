from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the website you want to load
url = "https://lab401.com/products/flipper-zero"

options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run the browser in headless mode
driver = webdriver.Chrome(options=options)

def get_page(url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'addToCart-product-template')))
    html_content = driver.page_source
    return html_content

def check_in_stock(html_content):
    if html_content.find("Notify me when in stock") != -1:
        print("out of stock")
    else:
        print("In stock")

url_page = get_page(url)
check_in_stock(url_page)


driver.quit()

