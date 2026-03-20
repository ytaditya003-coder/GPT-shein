import os
import time
import requests

# 1. Variables Load ho rahe hain
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URLS_STR = os.getenv('PRODUCT_URLS')

def send_test_message(msg):
    # Telegram API ko call karne ka tarika
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        r = requests.post(api_url, json=payload)
        # Logs mein dikhega ki Telegram ne kya bola
        print(f"--- Telegram Status: {r.status_code} ---")
        print(f"--- Response Detail: {r.text} ---")
        return r.status_code
    except Exception as e:
        print(f"--- Connection Error: {e} ---")
        return None

print("Checking Variables...")
print(f"Target Chat ID: {CHAT_ID}")

# Bot start hote hi sabse pehle ye chalega
status = send_test_message("🔔 TEST: Bot start ho gaya hai! Agar ye mila toh connection OK hai.")

if status == 200:
    print("SUCCESS: Message sent to Telegram!")
else:
    print("FAILURE: Message nahi gaya. Logs upar check karein.")

# Baki ka monitoring logic
if URLS_STR:
    urls = [u.strip() for u in URLS_STR.split(',') if u.strip()]
    while True:
        for url in urls:
            print(f"Scanning: {url}")
            try:
                res = requests.get(url, timeout=10)
                if "Sold Out" not in res.text and "Out of Stock" not in res.text:
                    send_test_message(f"🚨 STOCK ALERT!\n{url}")
            except:
                print("Error checking this link.")
        time.sleep(300)
        
