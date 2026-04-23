import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# --- CONFIGURATION ---
TARGET_LINK = "https://abr.ge/9gsx3c"
TOTAL_CLICKS_TO_DO = random.randint(10, 15) # Har run mein 10 se 15 clicks honge

def run_ultra_safe_bot():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    options.add_argument(f'--user-agent={ua}')

    print(f"🚀 Mission Started! Target: {TARGET_LINK}")
    print(f"📊 Goal for this session: {TOTAL_CLICKS_TO_DO} successful interactions.")
    print("-" * 40)

    try:
        driver_path = ChromeDriverManager().install()
        driver = uc.Chrome(options=options, driver_executable_path=driver_path)

        stealth(driver,
            user_agent=ua,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        success_count = 0

        for i in range(1, TOTAL_CLICKS_TO_DO + 1):
            try:
                driver.get(TARGET_LINK)
                time.sleep(random.randint(8, 12)) # Page load hone ka intezar
                
                # Scrolling to simulate human
                driver.execute_script(f"window.scrollBy(0, {random.randint(300, 700)});")
                
                # Second Click/Interaction logic
                wait = WebDriverWait(driver, 15)
                # Dhoondna Continue ya Get Link button
                buttons = driver.find_elements(By.XPATH, "//button | //a[contains(@href, 'http')] | //div[contains(@style, 'cursor: pointer')]")
                
                if buttons:
                    random.choice(buttons).click()
                    success_count += 1
                    print(f"✅ Click #{i}: Success! (Total: {success_count})")
                else:
                    print(f"⚠️ Click #{i}: Page loaded but no specific button found. Counting as view.")
                    success_count += 1

                # Har click ke baad lamba gap taake detect na ho (15-25 seconds)
                if i < TOTAL_CLICKS_TO_DO:
                    wait_time = random.randint(15, 25)
                    print(f"   Sleeping for {wait_time}s before next click...")
                    time.sleep(wait_time)

            except Exception as e:
                print(f"❌ Click #{i}: Failed due to small error. Continuing...")
                continue

        print("-" * 40)
        print(f"🏆 Session Finished! Total Successful Actions: {success_count}")

    except Exception as e:
        print(f"🛑 Critical Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_ultra_safe_bot()
