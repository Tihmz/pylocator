from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Run the browser in headless mode
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button___QH5tw.rounded-rect___yT8Yh.large___GUIHe.accent___uhads.large___GUIHe')))
    html_content = driver.page_source
    driver.quit()
    return html_content

def check_in_stock(html_content):
    if html_content.find("Ajouter au panier") != -1:
        return True
    elif html_content.find("Tout a déjà été vendu!") != -1:
        return False
