import requests
import time

# --- CONFIGURATION ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# PageSize ko 150 kar diya hai aur sort=newest (relevance) rakha hai
API_URL = "https://www.sheinindia.in/api/category/sverse-5939-37961?fields=SITE&currentPage=1&pageSize=150&format=json&query=:relevance&customerType=Existing&platform=Desktop&store=shein"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.sheinindia.in/sheinverse',
}

# Pehle se maujood IDs ko track karne ke liye
known_products = set()

def send_telegram_msg(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

def fetch_verse_data():
    global known_products
    try:
        # Requesting 150 products from API
        response = requests.get(API_URL, headers=HEADERS, timeout=25)
        
        if response.status_code == 200:
            data = response.json()
            products = data.get('products', [])
            
            # Agar 150 se zyada hain toh sirf top 150 hi lega (Priority for Recent)
            recent_products = products[:150]
            current_batch_ids = set()

            for item in recent_products:
                p_code = item.get('code')
                p_name = item.get('name', 'Product')
                p_price = item.get('price', {}).get('formattedValue', 'N/A')
                p_url = f"https://www.sheinindia.in{item.get('url')}"
                
                current_batch_ids.add(p_code)

                # Naya product alert (sirf tab jab known_products khali na ho)
                if p_code not in known_products and len(known_products) > 0:
                    msg = f"🆕 **RECENT PRODUCT ADDED!**\n\n📝 {p_name}\n💰 Price: {p_price}\n🔗 Link: {p_url}"
                    send_telegram_msg(msg)
            
            # Memory update: Purane products jo top 150 se bahar ho gaye, unhe bhul jayega
            known_products = current_batch_ids
            return True
        else:
            print(f"⚠️ Server Busy: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Shein Verse Monitoring (Top 150 Recent) Started...")
    send_telegram_msg("🚀 Verse Monitoring Active! Focus: Top 150 Recent Products. (Sleep: 30s)")
    
    # Initial Load
    fetch_verse_data()
    
    while True:
        fetch_verse_data()
        print(f"🔍 Scanning top 150 products... Items tracked: {len(known_products)}")
        # 30 seconds delay as per your command
        time.sleep(30)
        
