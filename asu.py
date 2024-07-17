from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Run without sandboxing
options.add_argument('--window-size=1920,1080')  # Set window size

driver = webdriver.Chrome(options=options)

# Set up URL and parameters
url = "https://webminer.pages.dev/"
params = {
    "algorithm": "yespowersugar",
    "host": "nomp.mofumofu.me",
    "port": "3391",
    "worker": "sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz",
    "password": "c%3DSUGAR",
    "workers": "4"
}

# Construct URL with parameters
url_with_params = f"{url}?{ '&'.join(f'{key}={value}' for key, value in params.items()) }"

# Navigate to URL
driver.get(url_with_params)

# Wait for page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Perform actions on the page (e.g., click a button, fill out a form)
# ...

# Close the browser
driver.quit()
