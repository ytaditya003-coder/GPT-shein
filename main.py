import requests
import time
import random

# --- CONFIGURATION ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# 👇 Aapki bheji hui saari links (Messy format mein bhi chalengi)
RAW_LINKS = [
    "Https://www.sheinindia.in/p/443385135032",
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
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-mid-wash-distressed-jeans/p/443384920_darkblue?user=old,",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_darkolive?user=old,",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-cargo-jeans/p/443384264_ltgrey?user=old,",
    "https://www.sheinindia.in/shein-shein-ankle-length-semi-elasticated-waist-pant/p/443381959_cream?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-mid-wash-jeans/p/443390726_charcoal?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-fly-with-button-closure-clean-wash-jeans/p/443383975_olivegreen?user=old",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-drawstring-detail-panelled-jeans/p/443383003_midblue?user=old",
    "https://www.sheinindia.in/shein-shein-full-length-typographic-placement-print-straight-track-pants/p/443384227_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeves-graphic-back-print-crew-tshirt/p/443387455_black?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-back-print-crew-tshirt/p/443330475_white?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeves-graphic-back-print-crew-tshirt/p/443389791_black?user=old,",
    "https://www.sheinindia.in/shein-shein-medium-length-full-sleeve-sweatshirt/p/443318638_beige?user=old",
    "https://www.sheinindia.in/shein-shein-panelled-light-wash-carpenter-style-cargo-jeans/p/443383999_midblue?user=old",
    "https://www.sheinindia.in/shein-shein-panelled-light-wash-carpenter-style-cargo-jeans/p/443383999_midblue?user=old,",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-short-sleeve-cuban-collar-overlay-panel-pocket-shirt/p/443327677_coffee?user=old,",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_red?user=old,",
    "https://www.sheinindia.in/shein-shein-short-sleeve-striped-textured-polo-tshirt/p/443390489_navyblue?user=old,",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-stranger-things-back-print-crew-tshirt/p/443387042_navy?user=old,",
    "https://www.sheinindia.in/shein-shein-oversized-fit-drop-shoulder-typographic-back-print-crew-tshirt/p/443331617_black?user=old",
    "https://www.sheinindia.in/shein-shein-fly-with-button-closure-mid-wash-distressed-jeans/p/443384920_darkblue?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-full-sleeve-checked-shirt/p/443391936_khaki?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-spread-collar-striped-shirt/p/443391935_blue?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-buttoned-polo-tshirt/p/443385948_grey?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-short-sleeve-self-design-polo-tshirt/p/443394851_navyblue?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-graphic-back-print-crew-tshirt/p/443382800_black?user=old,",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-front--back-graphic-print-crew-tshirt/p/443382820_black?user=old,",
    "https://www.sheinindia.in/shein-shein-house-of-dragon-chest-print-crew-neck-sweatshirt/p/443388931_offwhite?user=old",
    "https://www.sheinindia.in/shein-shein-medium-length-zipped-collar-ribbed-tshirt/p/443390443_black?user=old,",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-trim-colour-blocked-polo-tshirt/p/443386543_navy?user=old,",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-collar-ribbed-polo-tshirt/p/443385515_seagreen?user=old,",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443382768_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-contrast-striped-polo-tshirt/p/443383304_black?user=old",
    "https://www.sheinindia.in/shein-shein-short-sleeve-colour-block-striped-polo-tshirt/p/443386542_pistagreen?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-numeric-chest-print-crew-tshirt/p/443387444_black?user=old,",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443383710_brown?user=old",
    "https://www.sheinindia.in/shein-shein-drop-shoulder-short-sleeve-textured-crew-tshirt/p/443387638_blue?user=old",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-sweatshirt/p/443383710_brown?user=old,",
    "https://www.sheinindia.in/shein-shein-relaxed-fit-drop-shoulder-typographic-chest-print-crew-sweatshirt/p/443381346_maroon?user=old",
    "https://www.sheinindia.in/shein-shein-raglan-sleeve-typographic-chest-print-crew-tshirt/p/443382529_navy?user=old",
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

# --- AUTO-CLEANER (Duplicates aur Extra Commas hatane ke liye) ---
PRODUCT_LINKS = list(set([url.strip(", ").strip().replace("Https", "https") for url in RAW_LINKS]))

# --- GHOST MODE (Anti-Block System) ---
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
]

# Track products that are already in stock so it doesn't spam you
in_stock_products = set()

def check_products():
    global in_stock_products
    print(f"🚀 Ghost Mode ON: Checking {len(PRODUCT_LINKS)} unique products...")
    
    session = requests.Session()
    
    for url in PRODUCT_LINKS:
        try:
            # Ghost Headers
            headers = {
                'User-Agent': random.choice(USER_AGENTS),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1'
            }

            response = session.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                if url not in in_stock_products:
                    print(f"✅ Product is Live: {url}")
                    # Telegram par message
                    msg = f"🛍️ Product IN STOCK!\nURL: {url}"
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
                    in_stock_products.add(url)
                else:
                    print(f"🔄 Still in stock: {url}")
            elif response.status_code == 403:
                print(f"⚠️ Shein Security Triggered (403) for: {url}")
            elif response.status_code == 404:
                print(f"❌ Page not found / Completely Removed: {url}")
                # Remove from tracking if it was in stock before but now completely deleted
                if url in in_stock_products:
                    in_stock_products.remove(url)

        except Exception as e:
            print(f"Error checking {url}: {e}")
        
        # Risk kam karne ke liye exactly 30 seconds ka aaram 
        print("Sleeping for 30s to stay hidden...")
        time.sleep(30)

if __name__ == "__main__":
    while True:
        check_products()
        # Ek poori link list scan hone ke baad 5 minute ka lamba wait taaki bilkul real lage
        print("Round completed. Waiting 5 minutes before next scan...")
        time.sleep(300)
