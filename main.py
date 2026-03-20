import os
import time
import random
import requests
from bs4 import BeautifulSoup

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COOKIE = os.getenv('SHEIN_COOKIE')
WISHLIST_URL = os.getenv('WISHLIST_URL', 'https://www.sheinindia.in/wishlist')

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=10)
    except: pass

def check_wishlist():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
        'Cookie': COOKIE,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.sheinindia.in/',
        'Connection': 'keep-alive'
    }

    print(f"[{time.strftime('%H:%M:%S')}] 🕵️ Deep Scanning Wishlist...")
    
    try:
        response = requests.get(WISHLIST_URL, headers=headers, timeout=30)
        
        if "login" in response.url.lower():
            print("❌ Alert: Cookie Invalid! Refresh Cookie from Laptop.")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Sabhi tarah ke links dhoondna jo product ho sakte hain
        all_items = soup.find_all(['div', 'section', 'li'], class_=lambda x: x and ('item' in x.lower() or 'product' in x.lower()))
        
        if not all_items:
            # Last resort: try getting all links
            all_items = soup.select('a[href*="/p-"]')

        count = len(all_items)
        if count == 0:
            print("❓ Still 0 items. Checking if page content is blocked...")
            # Debugging: Print first 200 chars of page
            # print(response.text[:200]) 
            return

        print(f"✅ Scanning {count} potential items...")

        for item in all_items:
            text_content = item.get_text().lower()
            
            # Agar item mein 'out of stock' NAHI likha hai, toh alert bhejo
            if "out of stock" not in text_content and "sold out" not in text_content:
                # Sirf tab alert bhejo agar item mein price ya product jaisa kuch dikhe
                if "₹" in text_content or "off" in text_content:
                    print("✨ Stock Found!")
                    send_alert(f"🚀 <b>STOCK ALERT!</b>\n\nEk item stock mein dikh raha hai!\n\n🔗 <a href='{WISHLIST_URL}'>Open Wishlist</a>")
                    time.sleep(5) # Thoda gap
                    break # Ek baar mein ek alert kaafi hai

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("🚀 Master Stealth Bot Active!")
    while True:
        check_wishlist()
        wait = random.randint(180, 400)
        print(f"Next scan in {wait} seconds...")
        time.sleep(wait)
        
