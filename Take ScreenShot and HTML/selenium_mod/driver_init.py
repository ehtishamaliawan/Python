#from selenium.webdriver.firefox.options import Options
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from tempfile import mkdtemp


def init_driver():
    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920x1050")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.page_load_strategy = "normal"
    chrome_options.accept_insecure_certs = True
    chrome_options.binary_location = '/opt/chrome/chrome'
    
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    driver.set_page_load_timeout(30)
    return driver