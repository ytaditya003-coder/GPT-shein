import requests
import time
import random
import re

# --- AAPKI DETAILS ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# --- UNIQUE WEB PRODUCT LINKS ---
PRODUCT_LINKS = [
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443383652_royalblue",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443383652_bottlegreen",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-chest-print-crew-tshirt/p/443388774_black",
    "https://www.sheinindia.in/shein-shein-short-sleeves-contrast-striped-polo-tshirt/p/443330830_darkgreen",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-back-print-zipped-hoodie/p/443381800_darkgrey",
    "https://www.sheinindia.in/shein-shein-raglan-sleeve-typographic-chest-print-crew-tshirt/p/443382529_navy",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-front-print-crew-tshirt/p/443382829_stone",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-half-zipper-polo-tshirt/p/443329024_navy",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-back-print-crew-tshirt/p/443382837_navy",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-half-zipper-polo-tshirt/p/443329024_black",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-half-zipper-polo-tshirt/p/443329024_white",
    "https://www.sheinindia.in/shein-shein-short-sleeves-contrast-striped-polo-tshirt/p/443330830_black",
    "https://www.sheinindia.in/shein-shein-short-sleeves-contrast-striped-polo-tshirt/p/443330830_white",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-floral-print-crew-tshirt/p/443331451_black",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-floral-print-crew-tshirt/p/443331451_stone",
    "https://www.sheinindia.in/shein-shein-activewear-short-sleeve-graphic-front-and-back-print-crew-tshirt/p/443383142_white",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-typographic-placement-print-tshirt/p/443383311_beige",
    "https://www.sheinindia.in/shein-shein-party-medium-length-short-sleeve-sequins-style-shirt/p/443319394_maroon",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-typographic-chest-print-crew-tshirt/p/443331639_greymelange",
    "https://www.sheinindia.in/shein-shein-short-sleeve-self-design-contrast-trim-polo-tshirt/p/443386549_navy",
    "https://www.sheinindia.in/shein-shein-short-sleeve-self-design-contrast-trim-polo-tshirt/p/443386549_seagreen",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-medium-length-drop-shoulder-sweatshirt/p/443381777_blackmix",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-medium-length-drop-shoulder-sweatshirt/p/443381777_darkgrey",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-crew-sweatshirt/p/443381346_olivegreen",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-crew-sweatshirt/p/443381346_maroon",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443381773_darkgrey",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443383710_brown",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443387444_black",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443386542_pistagreen",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-striped-polo-tshirt/p/443383304_black",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443382768_black",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-zipped-ribbed-tshirt/p/443390484_brown",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-trim-colour-blocked-polo-tshirt/p/443386543_navy",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-ribbed-crew-tshirt/p/443391727_white",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-ribbed-crew-tshirt/p/443391727_lightblue",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-ribbed-crew-tshirt/p/443391727_brown",
    "https://www.sheinindia.in/shein-shein-baggy-fit-full-length-fly-with-button-closure-clean-jeans/p/443393702_charcoal",
    "https://www.sheinindia.in/shein-shein-panelled-light-wash-carpenter-style-cargo-jeans/p/443383999_midblue",
    "https://www.sheinindia.in/shein-shein-full-length-typographic-placement-print-straight-track-pants/p/443384227_black",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-front--back-graphic-print-crew-tshirt/p/443382820_black",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-back-print-crew-tshirt/p/443382800_black",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-drawstring-detail-panelled-jeans/p/443383003_midblue",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_khaki",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-striped-shirt/p/443391935_blue",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-ribbed-polo-tshirt/p/443390483_brown",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-clean-wash-jeans/p/443383975_olivegreen",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-mid-wash-jeans/p/443390726_charcoal",
    "https://www.sheinindia.in/shein-shein-ankle-length-semi-elasticated-waist-pant/p/443381959_cream",
    "https://www.sheinindia.in/shein-shein-short-sleeves-graphic-back-print-crew-tshirt/p/443389791_black",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_ltgrey",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_darkolive",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_red",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-short-sleeve-cuban-collar-overlay-panel-pocket-shirt/p/443327677_coffee",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-mid-wash-distressed-jeans/p/443384920_darkblue",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-print-crew-tshirt/p/443331617_black",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-stranger-things-back-print-crew-tshirt/p/443387042_navy",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-back-print-crew-tshirt/p/443388880_olive"
]

# --- ANTI-BLOCK USER AGENTS ---
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'
]

def send_telegram_msg(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=15)
    except Exception as e:
        print("❌ Telegram Message Failed:", e)

def check_stock_and_price(url, session):
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': 'en-US,en;q=0.9'
    }
    try:
        r = session.get(url, headers=headers, timeout=15)
        html_text = r.text.lower()
        
        # Out of stock check - "Sold Out" or "Notify Me" logic
        out_of_stock = "out of stock" in html_text or "sold out" in html_text
        
        if r.status_code == 200 and not out_of_stock:
            # Price extraction
            price_match = re.search(r'₹\s*([0-9,]+)', r.text)
            price = price_match.group(0) if price_match else "Site pe check karo"
            
            msg = f"🚀 **SUPER FAST STOCK ALERT!**\n\nBhai jaldi order kar, item wapas aa gaya!\n💰 Price: {price}\n🔗 Link: {url}"
            return msg
            
    except Exception as e:
        pass 
    return None

if __name__ == "__main__":
    print("🚀 Super Fast Monitoring Started...")
    send_telegram_msg("🚀 Bhai, Web Links ke sath Monitoring Shuru ho gayi hai! Sleep time 30s set hai.")

    session = requests.Session()

    while True:
        print(f"🔍 Checking {len(PRODUCT_LINKS)} products...")
        for url in PRODUCT_LINKS:
            alert = check_stock_and_price(url, session)
            
            if alert:
                send_telegram_msg(alert)
                print(f"✅ Alert sent for: {url}")
                
            # Random gap between links to stay safe (1-2 seconds)
            time.sleep(random.uniform(1, 2))
        
        print("⏳ Round complete. Resting for 30 seconds as requested...")
        time.sleep(30)
        
