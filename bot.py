import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

TARGET_LINKS = ["https://abr.ge/9gsx3c"]
PROXY_LIST = [f"proxy{i}.example.com:8080" for i in range(1, 101)]

def run_ultra_safe_bot():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    driver = uc.Chrome(options=options)

    try:
        url = TARGET_LINKS[0]
        driver.get(url)
        print(f"Page 1 loaded: {url}")
        
        # 1. Pehle page par thoda wait aur scroll
        time.sleep(random.randint(5, 8))
        driver.execute_script("window.scrollTo(0, 400);")

        # 2. DOUBLE CLICK LOGIC:
        # Ye niche wala part page par kisi bhi button ko dhoond kar click karega
        try:
            # Hum dhoond rahe hain koi bhi button ya link jo "Continue" ya "Get Link" jaisa ho
            wait = WebDriverWait(driver, 15)
            # Yahan hum common buttons ko target kar rahe hain
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button | //a[contains(@class, 'btn')]")))
            button.click()
            print("Successfully clicked the second button/link!")
            
            # Click ke baad 10-15 seconds rukna zaroori hai taake click count ho jaye
            time.sleep(random.randint(10, 15))
        except:
            print("No second button found, or already counted.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_ultra_safe_bot()
