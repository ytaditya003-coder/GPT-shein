import os
import time
import random
import requests
from bs4 import BeautifulSoup

# Railway se Variables uthana
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COOKIE = os.getenv('SHEIN_COOKIE')
WISHLIST_URL = os.getenv('WISHLIST_URL', 'https://www.sheinindia.in/wishlist')

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

def check_wishlist():
    # Opera Browser wala bhes (Stealth Mode)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
        'Cookie': COOKIE,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.sheinindia.in/',
        'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Opera";v="108", "Chromium";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'DNT': '1'
    }

    print(f"[{time.strftime('%H:%M:%S')}] 🕵️ Stealth Check Start...")
    
    try:
        response = requests.get(WISHLIST_URL, headers=headers, timeout=20)
        
        # Agar login page par redirect kare toh matlab Cookie fail hai
        if "login" in response.url.lower():
            print("❌ Alert: Cookie Expire ho gayi hai! Please update Railway.")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Wishlist ke products ko dhoondna
        products = soup.find_all('div', class_='S-product-item')
        
        if not products:
            print("❓ Wishlist khali hai ya page load nahi hua.")
            return

        for item in products:
            name_tag = item.find('a', class_='S-product-item__link')
            name = name_tag.text.strip() if name_tag else "Unknown Item"
            link = "https://www.sheinindia.in" + name_tag['href'] if name_tag else WISHLIST_URL
            
            # Stock check
            is_out_of_stock = item.find('div', class_='S-product-item__out-of-stock')
            
            if not is_out_of_stock:
                print(f"✨ STOCK FOUND: {name}")
                message = f"🚀 <b>QUICK STOCK ALERT!</b>\n\n<b>Item:</b> {name}\n\nAapki wishlist ka ye product stock mein aa gaya hai!\n\n🛒 <b>Order Now:</b> {link}"
                send_alert(message)
                time.sleep(random.uniform(1, 3)) # Insaan ki tarah gap

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print("🚀 Mega Stealth Bot Started for SHEIN!")
    while True:
        check_wishlist()
        
        # Random Wait Time (3 to 6 Minutes)
        wait_time = random.randint(180, 360) 
        print(f"Next check in {wait_time} seconds...")
        time.sleep(wait_time)
        
