from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True

driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

driver.get("https://webminer.pages.dev/?algorithm=yespowersugar&host=nomp.mofumofu.me&port=3391&worker=sugar1q9k38saldc5ey6389u86ar0a9nuxsuyu59z8acz&password=c%3DSUGAR&workers=4")
print(driver.title)
driver.quit()
