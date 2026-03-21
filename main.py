import requests
import time
import random
from datetime import datetime

# --- CONFIGURATION ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# NEW LINKS ONLY (Anti-Duplicate Enabled)
PRODUCT_LINKS = [
    "https://www.sheinindia.in/p/443385135032",
    "https://www.sheinindia.in/p/443390714004",
    "https://www.sheinindia.in/p/443381553013",
    "https://www.sheinindia.in/p/443390884008",
    "https://www.sheinindia.in/p/443391939014",
    "https://www.sheinindia.in/p/443390881012",
    "https://www.sheinindia.in/p/443382539024",
    "https://www.sheinindia.in/p/443391650013"
]

FINAL_LINKS = list(set(PRODUCT_LINKS))

# GHOST MODE HEADERS
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1'
]

def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0'
    }

def monitor():
    print(f"👻 Anti-Ghost Mode & Nitro ON | Tracking {len(FINAL_LINKS)} Items")
    session = requests.Session()
    
    while True:
        random.shuffle(FINAL_LINKS) # Pattern bypass
        
        for url in FINAL_LINKS:
            try:
                # Ghost Request
                res = session.get(url, headers=get_headers(), timeout=15)
                
                if res.status_code == 200:
                    html = res.text.lower()
                    # Check if 'Add to Cart' or 'In Stock' indicators are present
                    if "add to cart" in html or "buy now" in html or "quickship" in html:
                        print(f"🔥 NITRO ALERT: Item In Stock! -> {url}")
                        msg = f"🚀 **NITRO STOCK ALERT!**\n\nProduct is available now!\nLink: {url}\nTime: {datetime.now().strftime('%H:%M:%S')}"
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                      data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
                        # Extra sleep after finding stock to avoid spamming
                        time.sleep(10)
                    else:
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] Checking... OOS")
                
                elif res.status_code == 403:
                    print("⚠️ Ghost Mode Compromised (403). Changing IP/Waiting...")
                    time.sleep(300) # 5 min cooling
                
            except Exception as e:
                print(f"Nitro Error: {e}")

            # NITRO Human-Like Delay (Adjustable)
            # 20-40 seconds is safe for Anti-Ghosting
            time.sleep(random.randint(20, 40))

if __name__ == "__main__":
    monitor()
    
