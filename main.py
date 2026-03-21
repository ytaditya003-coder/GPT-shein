import requests
import time
import random

# --- CONFIGURATION ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# Aapki Saari Links (Duplicates Automatically Removed)
PRODUCT_LINKS = [
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443383652_royalblue?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443383652_bottlegreen?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-chest-print-crew-tshirt/p/443388774_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeves-contrast-striped-polo-tshirt/p/443330830_darkgreen?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-back-print-zipped-hoodie/p/443381800_darkgrey?user=old",
    "https://www.sheinindia.in/shein-shein-raglan-sleeve-typographic-chest-print-crew-tshirt/p/443382529_navy?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-front-print-crew-tshirt/p/443382829_stone?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-half-zipper-polo-tshirt/p/443329024_navy?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-back-print-crew-tshirt/p/443382837_navy?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-half-zipper-polo-tshirt/p/443329024_black?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-half-zipper-polo-tshirt/p/443329024_white?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeves-contrast-striped-polo-tshirt/p/443330830_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeves-contrast-striped-polo-tshirt/p/443330830_white?user=old",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-floral-print-crew-tshirt/p/443331451_black?user=old",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-floral-print-crew-tshirt/p/443331451_stone?user=old",
    "https://www.sheinindia.in/shein-shein-activewear-short-sleeve-graphic-front-and-back-print-crew-tshirt/p/443383142_white?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-typographic-placement-print-tshirt/p/443383311_beige?user=old",
    "https://www.sheinindia.in/shein-shein-party-medium-length-short-sleeve-sequins-style-shirt/p/443319394_maroon?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-typographic-chest-print-crew-tshirt/p/443331639_greymelange?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-self-design-contrast-trim-polo-tshirt/p/443386549_navy?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-self-design-contrast-trim-polo-tshirt/p/443386549_seagreen?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-medium-length-drop-shoulder-sweatshirt/p/443381777_blackmix?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-medium-length-drop-shoulder-sweatshirt/p/443381777_darkgrey?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-crew-sweatshirt/p/443381346_olivegreen?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-crew-sweatshirt/p/443381346_maroon?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443381773_darkgrey?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443383710_brown?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443387444_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443386542_pistagreen?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-striped-polo-tshirt/p/443383304_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443382768_black?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-zipped-ribbed-tshirt/p/443390484_brown?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-trim-colour-blocked-polo-tshirt/p/443386543_navy?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-ribbed-crew-tshirt/p/443391727_white?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-ribbed-crew-tshirt/p/443391727_lightblue?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-ribbed-crew-tshirt/p/443391727_brown?user=old",
    "https://www.sheinindia.in/shein-shein-baggy-fit-full-length-fly-with-button-closure-clean-jeans/p/443393702_charcoal?user=old",
    "https://www.sheinindia.in/shein-shein-panelled-light-wash-carpenter-style-cargo-jeans/p/443383999_midblue?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-typographic-placement-print-straight-track-pants/p/443384227_black?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-front--back-graphic-print-crew-tshirt/p/443382820_black?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-back-print-crew-tshirt/p/443382800_black?user=old",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-drawstring-detail-panelled-jeans/p/443383003_midblue?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_khaki?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-striped-shirt/p/443391935_blue?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-ribbed-polo-tshirt/p/443390483_brown?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-clean-wash-jeans/p/443383975_olivegreen?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-mid-wash-jeans/p/443390726_charcoal?user=old",
    "https://www.sheinindia.in/shein-shein-ankle-length-semi-elasticated-waist-pant/p/443381959_cream?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeves-graphic-back-print-crew-tshirt/p/443389791_black?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_ltgrey?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_darkolive?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_red?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-short-sleeve-cuban-collar-overlay-panel-pocket-shirt/p/443327677_coffee?user=old",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-mid-wash-distressed-jeans/p/443384920_darkblue?user=old",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-print-crew-tshirt/p/443331617_black?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-stranger-things-back-print-crew-tshirt/p/443387042_navy?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-back-print-crew-tshirt/p/443388880_olive?user=old"
]

# Clean list (Duplicates removed)
FINAL_LINKS = list(set(PRODUCT_LINKS))

# Anti-Block User Agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/122.0.0.0'
]

def monitor():
    print(f"🚀 Anti-Block Monitoring Started! Items: {len(FINAL_LINKS)}")
    session = requests.Session()
    
    while True:
        # Shuffle links har baar naya order
        random.shuffle(FINAL_LINKS)
        
        for url in FINAL_LINKS:
            try:
                headers = {
                    'User-Agent': random.choice(USER_AGENTS),
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Referer': 'https://www.google.com/',
                    'DNT': '1'
                }
                
                res = session.get(url, headers=headers, timeout=20)
                
                if res.status_code == 200:
                    content = res.text.lower()
                    # Stock Checking Logic
                    if "add to cart" in content or "buy now" in content:
                        print(f"🔥 IN STOCK: {url[:50]}...")
                        msg = f"✅ **STOCK ALERT!**\n\nProduct is back!\nLink: {url}"
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                      data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
                    else:
                        print(f"Checking: Out of Stock")
                
                elif res.status_code == 403:
                    print("⚠️ Forbidden (403) - Anti-Block Triggered! Sleeping for 10 mins...")
                    time.sleep(600) # 10 minute ka break
                
            except Exception as e:
                print(f"Connection Error: {e}")

            # Human-like Random Sleep (30 to 50 seconds)
            wait_time = random.randint(30, 50)
            time.sleep(wait_time)

if __name__ == "__main__":
    monitor()
