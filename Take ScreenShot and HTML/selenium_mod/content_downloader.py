# Importing required modules
import requests  
from selenium_mod.driver_init import init_driver


def download_content(url):
    try:
        r = requests.get(url)
        if r.status_code == 200 or r.status_code == 302:
            driver = init_driver()
            driver.set_page_load_timeout(60)
            try:
                driver.get(url)
            except Exception as e:
                driver.close()
                return "","",f"failed to access {url}: {e}"

            source_code = driver.page_source
            source_code = source_code.strip()

            driver.maximize_window()

            try:
                screenshot_png = driver.get_screenshot_as_png()
                driver.close()
                return source_code,screenshot_png,"success"
            except Exception as e:
                driver.close()
                return "","",f"failed to open {url}: {e}"
        else:
            return "","",f"failed to access {url} with status_code: {r.status_code}"
    except requests.exceptions.ConnectionError:
        return "","",f"{url} is dead/unreachable"
