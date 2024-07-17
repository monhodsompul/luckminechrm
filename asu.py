from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Jalankan Chrome di mode headless (opsional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to chromedriver
chromedriver_path = '/usr/bin/chromedriver'

# Inisialisasi WebDriver
driver = None

try:
    # Inisialisasi WebDriver
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

    # Mengakses sebuah website
    driver.get('https://webminer.pages.dev/?algorithm=yespowersugar&host=nomp.mofumofu.me&port=3391&worker=sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz&password=c%3DSUGAR&workers=4')

    # Mengambil judul halaman
    title = driver.title
    print(f'Title: {title}')

except WebDriverException as e:
    print(f'Selenium WebDriver Exception: {e}')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Menutup browser
    if driver:
        try:
            driver.quit()
        except WebDriverException:
            pass  # Abaikan jika sudah tertutup atau ada masalah lain saat menutup
