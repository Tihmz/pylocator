from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the website you want to load
url1 = 'https://www.joom.com/fr/products/62f661838ed09b01ebd4e0e2?variant_id=62f661838ed09b43ebd4e0e4'
#url2 = 'https://www.joom.com/fr/products/631b49363dd2930180ea74a7?variant_id=631b49363dd2931080ea74a9'
url2 = "https://www.joom.com/fr/products/631b4ab0a74fe601db26998a"

options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run the browser in headless mode
driver = webdriver.Chrome(options=options)

def get_page(url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button___QH5tw.rounded-rect___yT8Yh.large___GUIHe.accent___uhads.large___GUIHe')))
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button___QH5tw rounded-rect___yT8Yh large___GUIHe accent___uhads large___GUIHe')))
    html_content = driver.page_source
    return html_content

def check_in_stock(html_content):
    if html_content.find("Ajouter au panier") != -1:
        print("item in stock")
    elif html_content.find("Tout a déjà été vendu!") != -1:
        print("item hors stock")

url1_page = get_page(url1)
check_in_stock(url1_page)
url2_page = get_page(url2)
check_in_stock(url2_page)


driver.quit()

