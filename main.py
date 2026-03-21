import cloudscraper
import time
import os
import requests
import random
from datetime import datetime

# --- AAPKE RAILWAY VARIABLES KE SAATH MATCHING ---
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
COOKIE = os.environ.get("SHEIN_COOKIE")

TARGET_URL = "https://www.sheinindia.in/sheinverse/c/sverse-5939-37961?query=:relevance&classifier=intent"

def send_notification(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    try: requests.post(url, data=payload)
    except: pass

def monitor():
    print("🚀 Sheinverse New Product Monitor Started!")
    print(f"Settings: Sleep 30s | Cookie Stealth: {'ON' if COOKIE else 'OFF'}")
    
    scraper = cloudscraper.create_scraper(
        browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True}
    )
    
    if COOKIE:
        scraper.headers.update({'Cookie': COOKIE})

    last_content_hash = None

    while True:
        try:
            res = scraper.get(TARGET_URL, timeout=30)
            now = datetime.now().strftime('%H:%M:%S')
            
            if res.status_code == 200:
                # Page change check karne ke liye simple hash logic
                current_hash = hash(res.text)
                
                if last_content_hash is not None and current_hash != last_content_hash:
                    print(f"[{now}] 🔥 NEW PRODUCT DETECTED!")
                    send_notification(f"🚀 **NEW PRODUCT DETECTED!**\n\nSheinverse page update hua hai.\nLink: {TARGET_URL}")
                
                last_content_hash = current_hash
                print(f"[{now}] Checking... No new items.")
                time.sleep(30) # Aapka 30 sec sleep logic

            elif res.status_code == 403:
                print(f"[{now}] ⚠️ 403 Forbidden. WAF blocked. Waiting 10 mins...")
                time.sleep(600) 
            
            else:
                print(f"[{now}] Error {res.status_code}. Retrying...")
                time.sleep(60)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    # Ab ye check aapke Railway settings se match karega
    if not TOKEN or not CHAT_ID:
        print(f"❌ Error: Variables mismatch! TOKEN: {'OK' if TOKEN else 'MISSING'}, CHAT_ID: {'OK' if CHAT_ID else 'MISSING'}")
    else:
        monitor()
        
