import cloudscraper
import time
import os
import requests
import random
from datetime import datetime

# Railway Variables
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
COOKIE = os.environ.get("SHEIN_COOKIE") # Naya Variable

TARGET_URL = "https://www.sheinindia.in/sheinverse/c/sverse-5939-37961?query=:relevance&classifier=intent"

def send_notification(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    try: requests.post(url, data=payload)
    except: pass

def monitor():
    print("🚀 Ultra-Stealth Sheinverse Monitor Started!")
    
    # Custom Scraper with Cookies
    scraper = cloudscraper.create_scraper(
        browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True}
    )
    
    # Adding Cookie for authentication bypass
    if COOKIE:
        scraper.headers.update({'Cookie': COOKIE})
        print("✅ Cookie Loaded. Stealth Mode: ON")

    last_content_hash = None

    while True:
        try:
            # Random User-Agent change to avoid fingerprinting
            res = scraper.get(TARGET_URL, timeout=30)
            now = datetime.now().strftime('%H:%M:%S')
            
            if res.status_code == 200:
                current_hash = hash(res.text)
                if last_content_hash is not None and current_hash != last_content_hash:
                    print(f"[{now}] 🔥 NEW PRODUCT DETECTED!")
                    send_notification(f"🚀 **NEW PRODUCT DETECTED!**\n\nPage change detected on Sheinverse!\nLink: {TARGET_URL}")
                
                last_content_hash = current_hash
                print(f"[{now}] Success (200). Monitoring...")
                
                # Normal 30 sec sleep
                time.sleep(30) 

            elif res.status_code == 403:
                # Agar 403 aata hai toh lamba break lena zaruri hai
                wait_time = random.randint(600, 900) # 10-15 min break
                print(f"[{now}] ⚠️ Blocked (403). Waiting {wait_time//60} mins...")
                time.sleep(wait_time)
            
            else:
                print(f"[{now}] Error {res.status_code}. Retrying...")
                time.sleep(60)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    if not TOKEN or not CHAT_ID:
        print("❌ Error: Railway Variables missing!")
    else:
        monitor()
        
