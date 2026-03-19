import requests
from bs4 import BeautifulSoup
import time
import os

# Railway Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
PRODUCT_URL = os.getenv('PRODUCT_URL')

def check_stock():
    # Browser jaisa dikhne ke liye headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }
    
    try:
        response = requests.get(PRODUCT_URL, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Pure page ka text lower case mein convert karke check karna
        content = soup.get_text().lower()
        
        # Check if "Add to Bag" button is present or "Sold Out" is absent
        if "add to bag" in content or "add to cart" in content:
            # Check for common sold out phrases to be sure
            if "sold out" not in content and "out of stock" not in content:
                return True
        return False
    except Exception as e:
        print(f"Error checking site: {e}")
        return False

def send_telegram_msg(message):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🚨 **SHEIN UPDATE** 🚨\n\n{message}\n\nLink: {PRODUCT_URL}",
        "parse_mode": "Markdown"
    }
    requests.post(api_url, data=payload)

print("Bot started... Checking every 1 minute.")

while True:
    is_available = check_stock()
    
    if is_available:
        print("Item Available! Sending notification...")
        send_telegram_msg("🔥 Jaldi dekho! Aapka wishlist item STOCK mein aa gaya hai!")
        # Stock milne ke baad 10 minute break taaki spam na ho
        time.sleep(600) 
    else:
        print("Still out of stock. Waiting 60 seconds...")
        time.sleep(60) # 1 minute ka wait
