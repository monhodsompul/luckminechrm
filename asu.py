from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Applicable if running headless
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--remote-debugging-port=9222")  # Overcome limited resource problems

    # Set path to chromedriver as per your configuration
    webdriver_service = Service('/usr/bin/chromedriver')

    # Choose Chrome Browser
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    print("ChromeDriver has started successfully.")

    # Open the URL
    url = 'https://webminer.pages.dev/?algorithm=yespowersugar&host=nomp.mofumofu.me&port=3391&worker=sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz&password=c%3DSUGAR&workers=4'
    driver.get(url)
    print(f"Opened URL: {url}")

    # Wait for a specific element to load
    try:
        element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
        WebDriverWait(driver, 10).until(element_present)
        print("Page loaded successfully.")
    except Exception as e:
        print(f"Error waiting for page to load: {e}")

    # Print the title of the page
    print(f"Page title is: {driver.title}")

    # Keep the script running
    print("ChromeDriver will remain open. Press Ctrl+C to close.")
    while True:
        pass

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure driver is closed properly upon script termination
    if driver:
        driver.quit()
        print("ChromeDriver has closed successfully.")
