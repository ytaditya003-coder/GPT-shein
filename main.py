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
    # Final optimized API URL
    url = "https://www.sheinindia.in/api/wishlist/getwishlist?currentPage=1&pageSize=100"
    
    # Cookie ko clean up karna zaroori hai
    clean_cookie = COOKIE_STR.strip().replace('\n', '').replace('\r', '')
    
    # Bearer Token (A=) ko nikaalna
    bearer_token = ""
    if "A=" in clean_cookie:
        bearer_token = clean_cookie.split("A=")[1].split(";")[0]

    # Ye headers SHEIN ko lagega ki aap Browser se chala rahe ho
    headers = {
        'authority': 'www.sheinindia.in',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {bearer_token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.sheinindia.in/wishlist',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': clean_cookie
    }

    try:
        print("🕵️ Scanning Wishlist with Advanced Headers...")
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            print("✅ Status 200: Connection Successful!")
            data = response.json()
            products = data.get('info', {}).get('products', [])
            print(f"📊 Found {len(products)} total items in Wishlist.")
            # Stock checking logic yahan chalu hogi...
        else:
            print(f"❌ API Error: Status {response.status_code}")
            if response.status_code == 403:
                print("💡 Tip: Railway variable mein check karein ki 'A=' token sahi se copy hua hai.")
                
    except Exception as e:
        print(f"⚠️ Network Error: {e}")

if __name__ == "__main__":
    print("🔥 Master API Bot Active!")
    while True:
        check_wishlist()
        # Safe interval: 3 to 6 minutes
        wait_time = random.randint(180, 360)
        print(f"⏳ Next scan in {wait_time} seconds...")
        time.sleep(wait_time)
