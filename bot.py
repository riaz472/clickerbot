import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
import random

# --- CONFIGURATION ---
TARGET_LINKS = ["https://abr.ge/9gsx3c"]

# 100 Proxies (Yahan apni real proxies dalte rahein)
PROXY_LIST = [f"proxy{i}.example.com:8080" for i in range(1, 101)]

# Referers (Taake lage traffic direct nahi, balki social media se aayi hai)
REFERERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://t.co/", # Twitter
    "https://www.facebook.com/"
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
]

def run_ultra_safe_bot():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Random Screen Size (Real human ki tarah)
    res = random.choice(["1920,1080", "1366,768", "1536,864"])
    options.add_argument(f'--window-size={res}')

    ua = random.choice(USER_AGENTS)
    options.add_argument(f'--user-agent={ua}')

    if PROXY_LIST:
        proxy = random.choice(PROXY_LIST)
        if "example.com" not in proxy: # Check if user added real proxies
            options.add_argument(f'--proxy-server={proxy}')

    driver = uc.Chrome(options=options)

    stealth(driver,
        user_agent=ua,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        # Step 1: Pehle Google ya Twitter par jana (Safety)
        ref = random.choice(REFERERS)
        driver.get(ref)
        time.sleep(random.randint(2, 5))

        # Step 2: Asli Link par jana
        url = TARGET_LINKS[0]
        driver.get(url)
        print(f"Visited: {url} via {ref}")

        # --- SLOW ACTIONS (10-20 Clicks in 5 Mins) ---
        total_actions = random.randint(10, 20)
        for i in range(total_actions):
            # Smooth Scroll
            dist = random.randint(300, 600)
            driver.execute_script(f"window.scrollBy({{top: {dist}, behavior: 'smooth'}});")
            
            # Random Mouse Hover/Click
            try:
                body = driver.find_element(By.TAG_NAME, 'body')
                body.click()
            except:
                pass
            
            # Har action ke baad lamba gap (15-25 seconds)
            # Taake 5-6 minutes mein sirf 10-20 clicks hon
            time.sleep(random.uniform(15, 25))
            
            if i % 5 == 0: print(f"Progress: {i}/{total_actions} actions done.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Har baar script alag time pe shuru hogi
    time.sleep(random.randint(60, 300)) 
    run_ultra_safe_bot()
