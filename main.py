import os
import time
import random
import requests

# Railway Variables (Make sure these are set in Railway)
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

def add_to_cart(goods_id, sku_id, name):
    url = "https://www.sheinindia.in/api/cart/add"
    
    # Cookie string ko dictionary mein convert karna
    cookies = {pair.split('=')[0].strip(): pair.split('=')[1].strip() for pair in COOKIE_STR.split(';') if '=' in pair}
    
    payload = {
        "goods_id": goods_id,
        "sku_id": sku_id,
        "qty": 1,
        "type": 0
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': f'Bearer {cookies.get("A", "")}'
    }
    
    try:
        res = requests.post(url, json=payload, cookies=cookies, headers=headers, timeout=15)
        if res.status_code == 200:
            print(f"✅ Success: {name} added to cart!")
            send_telegram(f"🛍️ *AUTO-CART SUCCESS!*\n\nItem: {name}\n\nYeh item aapke bag mein daal diya gaya hai. Jaldi checkout karein!")
            return True
    except Exception as e:
        print(f"❌ Add to Cart Error: {e}")
    return False

def check_wishlist():
    url = "https://www.sheinindia.in/api/wishlist/getwishlist?currentPage=1&pageSize=100"
    
    cookies = {pair.split('=')[0].strip(): pair.split('=')[1].strip() for pair in COOKIE_STR.split(';') if '=' in pair}
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': f'Bearer {cookies.get("A", "")}'
    }

    try:
        print("🕵️ Scanning Wishlist...")
        response = requests.get(url, cookies=cookies, headers=headers, timeout=15)
        
        if response.status_code == 403:
            print("❌ API Error: Status 403 (Cookie Expired or Invalid)")
            return
            
        data = response.json()
        products = data.get('info', {}).get('products', [])
        
        in_stock_count = 0
        for p in products:
            name = p.get('name', 'SHEIN Item')
            goods_id = p.get('goods_id')
            
            # Check stock in variants
            for v in p.get('variantOptions', []):
                status = v.get('stock', {}).get('stockLevelStatus')
                if status == 'inStock':
                    in_stock_count += 1
                    sku_id = v.get('skuId')
                    # Automatically try to add to cart
                    add_to_cart(goods_id, sku_id, name)
                    
        print(f"📊 Found {in_stock_count} items in stock.")
        
    except Exception as e:
        print(f"⚠️ Scan Error: {e}")

if __name__ == "__main__":
    print("🚀 Auto-Cart Bot Started!")
    while True:
        check_wishlist()
        # Wait between 2 to 5 minutes to avoid ban
        wait_time = random.randint(120, 300)
        print(f"⏳ Next scan in {wait_time} seconds...")
        time.sleep(wait_time)
        
