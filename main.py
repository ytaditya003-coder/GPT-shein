import os
import time
import random
import requests

# Railway Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COOKIE_STR = os.getenv('SHEIN_COOKIE')

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=10)
    except:
        pass

def check_wishlist():
    # API URL
    url = "https://www.sheinindia.in/api/wishlist/getwishlist?currentPage=1&pageSize=100"
    
    # Cookie clean up
    clean_cookie = COOKIE_STR.strip().replace('\n', '').replace('\r', '')
    
    # Extract Bearer Token manually for safety
    bearer_token = ""
    if "A=" in clean_cookie:
        bearer_token = clean_cookie.split("A=")[1].split(";")[0]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': f'Bearer {bearer_token}',
        'Cookie': clean_cookie,
        'X-Requested-With': 'XMLHttpRequest'
    }

    try:
        print("🕵️ Scanning Wishlist...")
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 403:
            print("❌ API Error: Status 403 (Forbidden)")
            # Agar error aaye toh ek baar Telegram par batao
            return

        data = response.json()
        # Bakki logic same rahega...
        print("✅ Scan Successful!")
        
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    print("🔥 Master API Bot Active!")
    while True:
        check_wishlist()
        time.sleep(random.randint(180, 300))
