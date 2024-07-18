from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Mendefinisikan variabel driver di luar blok try
driver = None

try:
    # Mengatur opsi untuk menggunakan Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--no-sandbox')  # Menambahkan opsi no-sandbox

    # Menginisialisasi driver Selenium
    driver = webdriver.Chrome(options=options)

    # Membuka halaman web yang diminta
    driver.get("https://webminer.pages.dev/?algorithm=yespowersugar&host=nomp.mofumofu.me&port=3391&worker=sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz&password=c%3DSUGAR&workers=4")

except WebDriverException as e:
    print("Terjadi kesalahan: ", e)

finally:
    if driver is not None:
        driver.quit()
