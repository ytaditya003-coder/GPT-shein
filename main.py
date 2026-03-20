import os
import time
import random
import requests
import re
from bs4 import BeautifulSoup

# Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URLS_STR = os.getenv('PRODUCT_URLS')

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try: requests.post(url, json=payload)
    except: pass

def is_actually_in_stock(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    try:
        # 1. Page fetch karna (Redirects allow karke)
        response = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 2. Keywords check (Zyada strict)
        # SHEIN mobile site par aksar "Sold Out" ya "Coming Soon" niche buttons mein hota hai
        lowercase_html = html.lower()
        hidden_keywords = ["sold out", "out of stock", "item_status\":0", "is_on_sale\":false", "not_available"]
        
        for word in hidden_keywords:
            if word in lowercase_html:
                return False, None
        
        # 3. Price nikalna
        price = "Check Link"
        price_match = re.search(r'"amount":"(\d+\.?\d*)"', html)
        if price_match:
            price = f"₹{price_match.group(1)}"
            
        # 4. Final Check: Agar page par 'Add to Bag' ya 'Buy Now' dikh raha hai toh hi alert bhejo
        if "add to bag" in lowercase_html or "buy now" in lowercase_html:
            return True, price
            
        return False, None
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False, None

print("🚀 Mega Stealth Bot Started for SHEIN!")

while True:
    if URLS_STR:
        urls = [u.strip() for u in URLS_STR.split(',') if u.strip()]
        for url in urls:
            print(f"Scanning: {url}")
            in_stock, price = is_actually_in_stock(url)
            
            if in_stock:
                msg = (
                    f"✨ <b>PROUDCT BACK IN STOCK!</b> ✨\n\n"
                    f"💰 <b>Price:</b> {price}\n"
                    f"🔗 <a href='{url}'>JALDI KHARIDO!</a>\n\n"
                    f"<i>Bot is running in Super-Fast mode...</i>"
                )
                send_alert(msg)
                print("!!! ALERT SENT !!!")
            
            # Har link ke baad thoda gap
            time.sleep(random.randint(5, 8))
            
    # Cycle gap: 1 minute (Fastest for 1-2 min stock windows)
    time.sleep(60)
    
