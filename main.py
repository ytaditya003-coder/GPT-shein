import cloudscraper
import time
import os
import requests
from datetime import datetime

# --- CONFIGURATION FROM RAILWAY VARIABLES ---
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# Target URL for New Products
TARGET_URL = "https://www.sheinindia.in/sheinverse/c/sverse-5939-37961?query=:relevance&classifier=intent"

def send_notification(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending telegram msg: {e}")

def monitor_new_products():
    print("🚀 Sheinverse New Product Monitor Started!")
    print(f"Settings: Sleep 30s | Interval 4s")
    
    scraper = cloudscraper.create_scraper(
        browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True}
    )
    
    # Ismein hum purane products ke naam/ID save rakhenge
    known_products = set()
    first_run = True

    while True:
        try:
            res = scraper.get(TARGET_URL, timeout=30)
            now = datetime.now().strftime('%H:%M:%S')
            
            if res.status_code == 200:
                html_content = res.text.lower()
                
                # Simple logic: Humein product names ya unique strings dhoondne hain
                # Is URL par har product ka ek unique class ya ID hota hai
                # Hum abhi ke liye page ke content ko monitor kar rahe hain
                
                if first_run:
                    print(f"[{now}] Initial scan complete. Monitoring for changes...")
                    # Page ka initial state capture kar rahe hain
                    known_products.add(hash(html_content)) 
                    first_run = False
                else:
                    current_state = hash(html_content)
                    if current_state not in known_products:
                        print(f"[{now}] 🔥 NEW PRODUCT DETECTED!")
                        send_notification(f"🚀 **NEW PRODUCT DETECTED!**\n\nSheinverse page has been updated.\nLink: {TARGET_URL}")
                        known_products.add(current_state)
                    else:
                        print(f"[{now}] No new products. Sleeping...")

            elif res.status_code == 403:
                print(f"[{now}] ⚠️ 403 Forbidden. WAF blocked. Cooling down...")
                time.sleep(300) # 5 min rest if blocked

        except Exception as e:
            print(f"Error: {e}")

        # Aapka bataya hua timing logic: 30 sec sleep
        time.sleep(30)

if __name__ == "__main__":
    if not TOKEN or not CHAT_ID:
        print("❌ Error: TELEGRAM_BOT_TOKEN ya TELEGRAM_CHAT_ID Railway variables mein nahi mila!")
    else:
        monitor_new_products()
        
