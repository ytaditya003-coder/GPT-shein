import os
import time
import random
import requests

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COOKIE_STR = os.getenv('SHEIN_COOKIE')

# Browser list taaki SHEIN bot na pakad sake
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
]

def check_wishlist():
    url = "https://www.sheinindia.in/api/wishlist/getwishlist?currentPage=1&pageSize=100"
    
    clean_cookie = COOKIE_STR.strip().replace('\n', '').replace('\r', '')
    bearer_token = ""
    if "A=" in clean_cookie:
        bearer_token = clean_cookie.split("A=")[1].split(";")[0]

    headers = {
        'authority': 'www.sheinindia.in',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {bearer_token}',
        'user-agent': random.choice(USER_AGENTS),
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.sheinindia.in/wishlist',
        'cookie': clean_cookie
    }

    try:
        print("🕵️ Scanning Wishlist (Bypassing 403)...")
        # Timeout badha diya hai taaki slow network pe fail na ho
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            print("✅ Status 200: Connection Success!")
            # Stock logic...
        else:
            print(f"❌ Still getting Status {response.status_code}")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    print("🔥 Master API Bot Active!")
    while True:
        check_wishlist()
        # Scan gap badha diya hai taaki block na ho (5-8 minutes)
        time.sleep(random.randint(300, 500))
        
