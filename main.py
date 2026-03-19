import requests
from bs4 import BeautifulSoup
import time
import os

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
PRODUCT_URLS_STR = os.getenv('PRODUCT_URLS')

def check_stock(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text().lower()
        if ("add to bag" in content or "add to cart" in content) and ("sold out" not in content):
            return True
        return False
    except:
        return False

def send_notification(url):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🚨 **STOCK ALERT!**\n\nLink: {url}", "parse_mode": "Markdown"}
    requests.post(api_url, data=payload)

urls = [u.strip() for u in PRODUCT_URLS_STR.split(',')]
print(f"Monitoring {len(urls)} products.")

while True:
    for url in urls:
        if check_stock(url):
            send_notification(url)
            time.sleep(5)
    time.sleep(60)
    
