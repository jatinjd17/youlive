from selenium import webdriver
from time import sleep



from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=1920,1080')
options.add_argument("--headless")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# options.add_argument("--start-fullscreen")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# The place we will direct our WebDriver to


# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome(chrome_options=options)

# Directing the driver to the defined url
# driver.get('https://www.sps-software.net/')
driver.get('https://www.youtube.com/results?search_query=Shoutout+%21Wall+Show+your+Channel+Details+on+the+Fullscreen+Wall+with+your+Latest+4+Videos')

sleep(10)


driver.get('https://www.youtube.com/watch?v=ZHfK0EDBom8')

sleep(4)

print('runninggggggggggg')


sleep(5400)

driver.quit()
