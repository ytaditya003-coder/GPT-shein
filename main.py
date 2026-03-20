import os
import time
import random
import requests
from bs4 import BeautifulSoup

# Railway Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COOKIE_STR = os.getenv('SHEIN_COOKIE')
WISHLIST_API = "https://www.sheinindia.in/api/wishlist/getwishlist"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Telegram Error: {e}")

def get_wishlist():
    if not COOKIE_STR:
        print("❌ Error: SHEIN_COOKIE Variable is empty!")
        return []

    cookies = {}
    for pair in COOKIE_STR.split(';'):
        if '=' in pair:
            key, value = pair.strip().split('=', 1)
            cookies[key] = value

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Referer': 'https://www.sheinindia.in/',
        'Authorization': f'Bearer {cookies.get("A", "")}'
    }

    print(f"[{time.strftime('%H:%M:%S')}] 🕵️ API Scanning...")
    
    try:
        all_in_stock = []
        # Pehle 3 pages check karega (Jisme 60 products cover ho jayenge)
        for page in range(3):
            params = {'currentPage': page, 'pageSize': 20}
            response = requests.get(WISHLIST_API, params=params, cookies=cookies, headers=headers, timeout=15)
            
            if response.status_code != 200:
                print(f"API Error: Status {response.status_code}")
                break

            data = response.json()
            products = data.get('products', [])
            if not products: break

            for p in products:
                name = p.get('name', 'SHEIN Item')
                in_stock = False
                size_info = ""
                
                if 'variantOptions' in p:
                    for v in p['variantOptions']:
                        if v.get('stock', {}).get('stockLevelStatus') == 'inStock':
                            in_stock = True
                            # Size nikalna
                            for q in v.get('variantOptionQualifiers', []):
                                if q.get('qualifier') == 'size':
                                    size_info += f"[{q.get('value')}] "

                if in_stock:
                    all_in_stock.append(f"✨ *{name}*\nSizes: {size_info}")

        return all_in_stock
    except Exception as e:
        print(f"Scan Error: {e}")
        return []

if __name__ == "__main__":
    print("🔥 Master API Bot Active!")
    last_seen = set()

    while True:
        items = get_wishlist()
        print(f"Found {len(items)} items currently in stock.")

        for item in items:
            if item not in last_seen:
                send_telegram(f"🔔 *IN-STOCK ALERT!*\n\n{item}\n\n🛒 [Open Wishlist](https://www.sheinindia.in/wishlist)")
                last_seen.add(item)
        
        # 4 to 8 minutes wait
        wait_time = random.randint(240, 480)
        print(f"Next scan in {wait_time} seconds...")
        time.sleep(wait_time)
        
