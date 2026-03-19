import requests
from bs4 import BeautifulSoup
import time
import os

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
PRODUCT_URLS_STR = os.getenv('PRODUCT_URLS')

# Links ko list mein badalna
PRODUCT_URLS = [url.strip() for url in PRODUCT_URLS_STR.split(',') if url.strip()]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def check_stock(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text().lower()
        if "sold out" not in content and "out of stock" not in content:
            return True
        return False
    except:
        return False

# Sabse pehle /start ka reply dega
send_telegram_message("sunn rha behra nahi hu mai")

print(f"Bot Active! Monitoring {len(PRODUCT_URLS)} products...")

while True:
    for url in PRODUCT_URLS:
        if check_stock(url):
            send_telegram_message(f"🚨 STOCK ALERT! 🚨\n\nItem is BACK! Jaldi check karo:\n{url}")
            # Stock milne par list se hata sakte hain ya rehne dein (abhi rehne diya hai)
        time.sleep(15)  # Har product ke beech delay
    
    print("Cycle complete. Sleeping for 5 minutes...")
    time.sleep(300)
    
