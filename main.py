import requests
import time
import random
import re

# --- AAPKI DETAILS ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# --- SAARE PRODUCTS KI LIST ---
PRODUCT_LINKS = [
    "https://www.sheinindia.in/p/443385135032",
    "https://www.sheinindia.in/p/443390714004",
    "https://www.sheinindia.in/p/443381553013",
    "https://www.sheinindia.in/p/443390884008",
    "https://www.sheinindia.in/p/443391939014",
    "https://www.sheinindia.in/p/443390881012",
    "https://www.sheinindia.in/p/443382539024",
    "https://www.sheinindia.in/p/443391650013",
    "https://www.sheinindia.in/p/443386275012",
    "https://www.sheinindia.in/p/443393028017",
    "https://www.sheinindia.in/p/443389781002",
    "https://www.sheinindia.in/p/443383954007",
    "https://www.sheinindia.in/p/443383392010",
    "https://www.sheinindia.in/p/443385416012",
    "https://www.sheinindia.in/p/443388018014",
    "https://www.sheinindia.in/p/443382000006",
    "https://www.sheinindia.in/p/443392033002",
    "https://www.sheinindia.in/p/443316334002",
    "https://sheinindia.onelink.me/ZrSt/uiuzq9hx",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-mid-wash-distressed-jeans/p/443384920_darkblue",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_darkolive",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_ltgrey",
    "https://www.sheinindia.in/shein-shein-ankle-length-semi-elasticated-waist-pant/p/443381959_cream",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-mid-wash-jeans/p/443390726_charcoal",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-clean-wash-jeans/p/443383975_olivegreen",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-drawstring-detail-panelled-jeans/p/443383003_midblue",
    "https://www.sheinindia.in/shein-shein-full-length-typographic-placement-print-straight-track-pants/p/443384227_black",
    "https://www.sheinindia.in/shein-shein-short-sleeves-graphic-back-print-crew-tshirt/p/443387455_black",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-back-print-crew-tshirt/p/443330475_white",
    "https://www.sheinindia.in/shein-shein-short-sleeves-graphic-back-print-crew-tshirt/p/443389791_black",
    "https://www.sheinindia.in/shein-shein-medium-length-full-sleeve-sweatshirt/p/443318638_beige",
    "https://www.sheinindia.in/shein-shein-panelled-light-wash-carpenter-style-cargo-jeans/p/443383999_midblue",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-short-sleeve-cuban-collar-overlay-panel-pocket-shirt/p/443327677_coffee",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_red",
    "https://www.sheinindia.in/shein-shein-short-sleeve-striped-textured-polo-tshirt/p/443390489_navyblue",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-stranger-things-back-print-crew-tshirt/p/443387042_navy",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-print-crew-tshirt/p/443331617_black",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_khaki",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-striped-shirt/p/443391935_blue",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-buttoned-polo-tshirt/p/443385948_grey",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-self-design-polo-tshirt/p/443394851_navyblue",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-back-print-crew-tshirt/p/443382800_black",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-front--back-graphic-print-crew-tshirt/p/443382820_black",
    "https://www.sheinindia.in/shein-shein-house-of-dragon-chest-print-crew-neck-sweatshirt/p/443388931_offwhite",
    "https://www.sheinindia.in/shein-shein-medium-length-zipped-collar-ribbed-tshirt/p/443390443_black",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-trim-colour-blocked-polo-tshirt/p/443386543_navy",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-collar-ribbed-polo-tshirt/p/443385515_seagreen",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443382768_black",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-striped-polo-tshirt/p/443383304_black",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443386542_pistagreen",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443387444_black",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443383710_brown",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-textured-crew-tshirt/p/443387638_blue",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-crew-sweatshirt/p/443381346_maroon",
    "https://www.sheinindia.in/shein-shein-raglan-sleeve-typographic-chest-print-crew-tshirt/p/443382529_navy"
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
        
        # Out of stock check
        out_of_stock = "out of stock" in html_text or "sold out" in html_text
        
        if r.status_code == 200 and not out_of_stock:
            # Price dhoondhne ki koshish
            price_match = re.search(r'₹\s*([0-9,]+)', r.text)
            price = price_match.group(0) if price_match else "Site pe check karo"
            
            msg = f"🚀 **FAST STOCK ALERT!**\n\nBhai jaldi order kar, item wapas aa gaya!\n💰 Price: {price}\n🔗 Link: {url}"
            return msg
            
    except Exception as e:
        pass # Ignore slow connection errors so bot doesn't stop
    return None

if __name__ == "__main__":
    print("🚀 Fast & Stealth Monitoring Started...")
    send_telegram_msg("Bhai, nayi ID ke sath aapka bot LIVE ho gaya hai! Ab ye saare links par nazar rakhega.")

    session = requests.Session()

    while True:
        print("🔍 Checking all products...")
        for url in PRODUCT_LINKS:
            alert = check_stock_and_price(url, session)
            
            if alert:
                send_telegram_msg(alert)
                print(f"✅ Alert sent for: {url}")
                
            # Har link check karne ke beech 1-3 second ka gap (Anti-Block)
            time.sleep(random.uniform(1, 3))
        
        print("⏳ Ek poora round khatam. 2 minute baad dubara check karunga...")
        # Poori list check hone ke baad 2 minute (120 seconds) rukega
        time.sleep(120)
        
