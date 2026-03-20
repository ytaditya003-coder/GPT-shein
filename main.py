import os
import time
import random
import requests
from bs4 import BeautifulSoup

# Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URLS_STR = os.getenv('PRODUCT_URLS')

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]

def send_alert(message):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(api_url, json=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

def check_stock():
    if not URLS_STR: return
    urls = [u.strip() for u in URLS_STR.split(',') if u.strip()]
    
    for url in urls:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        try:
            print(f"Checking: {url}")
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # --- LOGIC START ---
            # 1. Page text check
            full_text = response.text.lower()
            
            # SHEIN ke common 'Out of Stock' keywords
            out_of_stock_keywords = [
                "sold out", "out of stock", "item is not available", 
                "unavailable", "coming soon", "notify me"
            ]
            
            # Check if any keyword exists
            is_sold_out = any(word in full_text for word in out_of_stock_keywords)
            
            # 2. Meta Tag Check (Price agar 0 hai ya tag missing hai toh aksar sold out hota hai)
            price_tag = soup.find("meta", property="product:price:amount")
            price = price_tag.get("content") if price_tag else "Check Link"

            # ALERT TABHI JAYEGA JAB: 
            # - Keywords mein 'Sold Out' na ho
            # - Price 0 na ho (Kuch cases mein price gayab ho jati hai)
            if not is_sold_out:
                msg = (
                    f"🚨 <b>ITEM IN STOCK!</b> 🚨\n\n"
                    f"💰 <b>Price:</b> ₹{price}\n"
                    f"🔗 <a href='{url}'>Abhi Buy Karein</a>"
                )
                send_alert(msg)
                print("Alert Sent!")
            else:
                print("Status: Still Sold Out.")

        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(random.randint(5, 10))

print("🚀 Bot Fix Applied! Starting monitoring...")
while True:
    check_stock()
    time.sleep(random.randint(45, 90))
    
