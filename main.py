import requests
import time
import random
from datetime import datetime

# --- CONFIGURATION ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# Nayi Clean Links
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

# STEALTH USER AGENTS
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1'
]

def get_stealth_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

def monitor():
    print(f"🕵️ Ultra-Stealth Mode Active | Tracking {len(FINAL_LINKS)} Items")
    session = requests.Session()
    
    while True:
        random.shuffle(FINAL_LINKS) # Har baar order badlega
        
        for url in FINAL_LINKS:
            try:
                headers = get_stealth_headers()
                res = session.get(url, headers=headers, timeout=20)
                
                now = datetime.now().strftime('%H:%M:%S')
                
                if res.status_code == 200:
                    html = res.text.lower()
                    if "add to cart" in html or "buy now" in html:
                        print(f"[{now}] 🔥 STOCK FOUND: {url}")
                        msg = f"✅ **STOCK ALERT!**\n\nItem is available!\nLink: {url}"
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                      data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
                        time.sleep(15) # Found ke baad thoda break
                    else:
                        print(f"[{now}] Checking... Still Out of Stock")
                
                elif res.status_code == 403:
                    print(f"[{now}] ⚠️ 403 Forbidden! Shein is watching. Sleeping for 15 mins...")
                    time.sleep(900) # Block aane par seedha 15 min ka gap
                    break # Loop se bahar nikal kar naya session banayenge
                
            except Exception as e:
                print(f"Error: {e}")

            # STEALTH SLEEP (120 to 240 seconds - yani 2 se 4 minute ka gap)
            wait = random.randint(120, 240)
            print(f"Next check in {wait} seconds...")
            time.sleep(wait)

if __name__ == "__main__":
    monitor()
    
