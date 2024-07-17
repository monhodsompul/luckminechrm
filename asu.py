from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

url = "https://webminer.pages.dev/"
params = {
    "algorithm": "yespowersugar",
    "host": "nomp.mofumofu.me",
    "port": "3391",
    "worker": "sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz",
    "password": "c%3DSUGAR",
    "workers": "4"
}

url_with_params = f"{url}?{ '&'.join(f'{key}={value}' for key, value in params.items()) }"

try:
    driver.get(url_with_params)
    print("Page loaded successfully")
    time.sleep(5)  # give the page some time to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Page fully loaded")
    # Perform actions on the page (e.g., click a button, fill out a form)
    #...
    input("Press Enter to close...")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
