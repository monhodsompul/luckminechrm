from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
# Hapus opsi --headless jika ingin melihat browser
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Menggunakan WebDriverManager untuk mengelola ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Mengakses web miner
    driver.get('https://webminer.pages.dev/?algorithm=yespowersugar&host=nomp.mofumofu.me&port=3391&worker=sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz&password=c%3DSUGAR&workers=4')

    # Mengambil judul halaman
    title = driver.title
    print(f'Title: {title}')

    # Tunggu sampai browser ditutup secara manual
    input("Press Enter to close the browser...")

except Exception as e:
    print(f'Error: {e}')

finally:
    # Jangan menutup browser otomatis
    pass
