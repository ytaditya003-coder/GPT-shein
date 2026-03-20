import os
import time
import random
import requests
from bs4 import BeautifulSoup

# Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URLS_STR = os.getenv('PRODUCT_URLS')

# Fake Browsers ki list (Taaki SHEIN block na kare)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
]

def send_alert(message):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(api_url, json=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

def check_stock():
    if not URLS_STR:
        return
        
    urls = [u.strip() for u in URLS_STR.split(',') if u.strip()]
    
    for url in urls:
        # Har request mein random browser aur thoda delay lagayenge taaki ban na ho
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
        
        try:
            print(f"Scanning: {url}")
            response = requests.get(url, headers=headers, timeout=15)
            
            # Agar SHEIN ne block kiya toh code 403 aayega
            if response.status_code == 403:
                print("Warning: SHEIN rate limit hit. Sleeping longer...")
                time.sleep(30)
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = soup.get_text().lower()

            # "Out of stock" ya "Sold out" check karna
            is_out_of_stock = "sold out" in page_text or "out of stock" in page_text

            # Agar product stock mein hai!
            if not is_out_of_stock:
                # Price dhoondne ki koshish (Meta tags se)
                price = "Not Found"
                price_tag = soup.find("meta", property="og:price:amount") or soup.find("meta", property="product:price:amount")
                if price_tag and price_tag.get("content"):
                    price = f"₹{price_tag.get('content')}"

                # Size dhoondne ki koshish (Usually selected size ya available sizes)
                # Note: SHEIN sizes JS se load karta hai, par hum basic HTML size tags dhoondte hain
                size_info = "Available (Check link for exact size)"
                
                # Telegram par mast sa message bhejna
                msg = (
                    f"🚨 <b>SHEIN STOCK ALERT!</b> 🚨\n\n"
                    f"📦 <b>Status:</b> IN STOCK\n"
                    f"💰 <b>Price:</b> {price}\n"
                    f"📏 <b>Size:</b> {size_info}\n\n"
                    f"🛒 <b>Jaldi kharido:</b> <a href='{url}'>Click Here</a>"
                )
                
                send_alert(msg)
                print(f"STOCK MIL GAYA! Message sent for {url}")
                
        except Exception as e:
            print(f"Error reading {url}: {e}")

        # Har link check karne ke beech mein 3 se 7 second ka random gap (Anti-Ban)
        time.sleep(random.uniform(3.0, 7.0))

# --- MAIN LOOP ---
print("🚀 Advanced Stealth Bot Started!")
send_alert("✅ <b>Advanced Bot Active!</b>\nMain ab full speed aur stealth mode mein items check kar raha hoon.")

while True:
    check_stock()
    # Har cycle ke baad 45 se 90 seconds (1-1.5 min) ka random sleep, jisse site pakad na paaye
    sleep_time = random.randint(45, 90)
    print(f"Cycle complete. Sleeping for {sleep_time} seconds to avoid ban...")
    time.sleep(sleep_time)
    
