import os
import time
import random
import requests
import json

# Railway Variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COOKIE_STR = os.getenv('SHEIN_COOKIE')

# API Settings (From your file)
WISHLIST_API = "https://www.sheinindia.in/api/wishlist/getwishlist"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=10)
    except:
        pass

def get_wishlist():
    # Cookie string ko format mein badalna
    cookies = {}
    for pair in COOKIE_STR.split(';'):
        if '=' in pair:
            key, value = pair.strip().split('=', 1)
            [span_2](start_span)cookies[key] = value[span_2](end_span)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        [span_3](start_span)'Accept': 'application/json',[span_3](end_span)
        [span_4](start_span)'Referer': 'https://www.sheinindia.in/',[span_4](end_span)
        [span_5](start_span)'Authorization': f'Bearer {cookies.get("A", "")}'[span_5](end_span)
    }

    print(f"[{time.strftime('%H:%M:%S')}] 🚀 API Scanning Started...")

    try:
        # API se data nikalna (Page 0 se 5 tak check karega)
        all_in_stock = []
        for page in range(5): 
            [span_6](start_span)params = {'currentPage': page, 'pageSize': 20}[span_6](end_span)
            response = requests.get(WISHLIST_API, params=params, cookies=cookies, headers=headers, timeout=15)
            
            if response.status_code != 200:
                break

            data = response.json()
            [span_7](start_span)products = data.get('products', [])[span_7](end_span)
            
            if not products:
                break

            for p in products:
                [span_8](start_span)name = p.get('name', 'SHEIN Item')[span_8](end_span)
                # Stock level check karna
                in_stock = False
                size_info = ""
                
                [span_9](start_span)if 'variantOptions' in p:[span_9](end_span)
                    [span_10](start_span)for v in p['variantOptions']:[span_10](end_span)
                        [span_11](start_span)if v.get('stock', {}).get('stockLevelStatus') == 'inStock':[span_11](end_span)
                            in_stock = True
                            [span_12](start_span)size = next((q['value'] for q in v.get('variantOptionQualifiers', []) if q['qualifier'] == 'size'), 'N/A')[span_12](end_span)
                            size_info += f"[{size}] "

                if in_stock:
                    all_in_stock.append(f"✨ *{name}*\nSizes: {size_info}")

        return all_in_stock

    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    print("🔥 API Stealth Monitor Active!")
    last_seen = set()

    while True:
        items = get_wishlist()
        print(f"Found {len(items)} items in stock.")

        for item in items:
            if item not in last_seen:
                send_telegram(f"🔔 *IN-STOCK ALERT!*\n\n{item}\n\n🛒 [Open Wishlist](https://www.sheinindia.in/wishlist)")
                last_seen.add(item)

        # 3 to 7 minutes gap (Safe mode)
        wait = random.randint(180, 420)
        print(f"Next scan in {wait} seconds...")
        time.sleep(wait)
        
