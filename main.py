import requests
import time

# --- TELEGRAM CONFIG ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# --- SHEIN API ---
API_URL = "https://www.sheinindia.in/api/category/sverse-5939-37961?fields=SITE&currentPage=1&pageSize=150&format=json&query=:relevance"

# --- ARRANGED COOKIE (Cleaned for Python) ---
RAW_COOKIE = """V=1; bm_ss=ab8e18ef4e; _fpuuid=yk5W46eCYJYIvcwV9D0c2; deviceId=yk5W46eCYJYIvcwV9D0c2; EI=mcqJQvYOa0UyB7gpill1of8U6vpbLKn1clO%2BOcZuDmLBGnmQsymHC8huZb2WDcEQ; mE=she***************%40gmail.com; mN=91XXXXX560; uI=9198308560; un=aditya%20; MN=9198308560; CI=eb45c64f-699e-4ab7-87c0-712ad6df934f; PK=2O9VKB0%2B%2BKGPGSCWCnKwqWleYJP94kolBaFF8jQqrpLVFyTNSPJL4LAcaOQy5%2B31; SN=aditya; G=M; A=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzaGVpbl9hZGl0eWFyYW9yYmpAZ21haWwuY29tIiwicGtJZCI6ImViNDVjNjRmLTY5OWUtNGFiNy04N2MwLTcxMmFkNmRmOTM0ZiIsImNsaWVudE5hbWUiOiJ3ZWJfY2xpZW50Iiwicm9sZXMiOlt7Im5hbWUiOiJST0xFX0NVU1RPTUVSR1JPVVAifV0sIm1vYmlsZSI6IjkxOTgzMDg1NjAiLCJ0ZW5hbnRJZCI6IlNIRUlOIiwiZXhwIjoxNzc2MDEyMDMwLCJ1dWlkIjoiZWI0NWM2NGYtNjk5ZS00YWI3LTg3YzAtNzEyYWQ2ZGY5MzRmIiwiaWF0IjoxNzczNDIwMDMwLCJlbWFpbCI6ImFkaXR5YXJhb3JiakBnbWFpbC5jb20ifQ.U7yf-GMwLIXB9sZjNcixEhevk0YirrELcYJEICxNqusv3bdNY74GkKhtAPLXC5dL9MMfkPB7L_yqhCBkqyzk-oaA6eCya7K0Z1VrZY4usMusxIr_I9o0Bb3PqHjfw7mVudgCJNRveV-On45OEPg4Oj45gw-0xCWINWEfDJ08dnVMf9HbYnJqAepYbapeL1IH8YZ6gQCsmc0JFgWb6HbF3OkZ5f-HD_pu_TykBCPXAF0AvrELATteoD0EoRKy5vwCa_vinabKGg5RScTIrbc1U7I1zIvPEEz62g4SMnvoSTBJ3S9LUI2HCa5BlyljpjVnnr36UZvUySAn-XgMITubaw; U=adityaraorbj%40gmail.com; LS=LOGGED_IN; R=eyJhbGciOiJSUzI1NiJ9.eyJzZXNzaW9uIjp7InNlc3Npb25JZCI6ImYyYjIwMzEwLTU4MWUtNDAxYi05OTA5LTg1N2RhMWU3Y2I3NiIsImNsaWVudE5hbWUiOiJ3ZWJfY2xpZW50Iiwicm9sZXMiOlt7Im5hbWUiOiJST0xFX0NVU1RPTUVSR1JPVVAifV19LCJ0eXBlIjoicmVmcmVzaCIsInRlbmFudElkIjoiU0hFSU4iLCJzdWIiOiJzaGVpbl9hZGl0eWFyYW9yYmpAZ21haWwuY29tIiwiZXhwIjoxNzg4OTcyMDMwLCJpYXQiOjE3NzM0MjAwMzB9.dWHJzJycwCEF_sQwcfygrBd31rVrerLvxAP9-E2sa_bWENNI3To3fmA3lvOhHhDwdtPFvoxpeoS6a-8WVG8LjIXAB5C6qIC9nVIYE2iVhireyTUI3251-hJjm5hk_pEsQOklQKIsrKgm8F0CCppdISaW2lNUD6WC6lO8-Z5Z7HYQzF1F1JV4tEtYSc3ncf5jtWOWkpwz8J4cD1Sox52ndCRKUqgp7J4Jgyh-Xt4V5M1WHbUrsJIICai7Cpwl2g3Y_Dp-EDMDmuyrwFNbJCnaNuB4UBiSU1tiyzF6DjOIGwxZiwE326AxO5aNzIhORLcpwBVTJw4E3lJoTC6dPQv9Dw; M=SH9237708413; GUID=18f80a8b-972e-42e2-925a-a6ca4e080dd7; C=SH9237708413; customerType=Existing; cohortSegment=17,19,10; jioAdsFeatureVariant=true; CT=ALLAHABAD; ST=UTTAR PRADESH; ZN=undefined; PG=; sessionId=sess_1774084100789_pe7ljyonp; bm_mi=1B00A6F5449BADDB20D4B641B335961F~YAAQP7sbuDw2k/ecAQAAjxWnDx/LJoQHZMS4NKM5RaOLSpcUjcmNy+4OxQeY2oeEkG8nm2Gbbr8RWyoDDc4I9Ur2cPmzQl7RDLvQPMwL1VZ/uTXlYaVKJ65eroWUnqSsXjBpF/jDn0pKBdakCvESfjWI2DI0MNaLOLyy5D/XEz+LNm16O3XD1CcRK+krlgVhe77K0zmZwmRKyQSkPwAfGdJF/UUM6zl+EHNTYPREsoAOECBe97ZDiHBe5jxlIIB4Adj6DIVsBZS210F1HC+y5m7Pk48wYL+xFXW7iacxF7H+KDD29d5XKJ6s1HoPPzDzCiAU7QM3ytSmGMKbmYK48zcXExE3X9h5uSSLdlRw~1; _abck=348D0332D3095B2C68C9D02F7B648787~0~YAAQP7sbuE42k/ecAQAA6RanDw/ZoSxcnjsXVFrbh1rJea4FJ99+9FGAqRa5OAJOtzVUrsCtMH5zfDDKDmbriBfbNYUluX7jBOXtKKboZ+gFFnbrql6zAupnTQ0y++h7tSsXqgRIAyTnL8oXenmk/Qe3gPucUaZs23VULKnDI+yKE2Q8aP1nqlsodQu/FWfTc5xVPPnFtx+tYpYqTWy34BWCTirXpqNn5Xwf4BMGJVqhlB3yWWJ2mDv/8WZiQu17Uxj7XvPA8jHY4Pp7IrZv2qdZ0umhxQ006NzM0f4Zfj5qukdEdYk9A374+hAdgMZcm35PClY/lbHP/3QAR0gUi4wYuYbzEX4rd8XEYhW5spexiqm8LBAJXdLOxWaqlwXzK42WiDhb2I40KBu+QHlk4gfkX+yP7snwfbZ+NsdlI2rSc6BFMwipmUHIP+9Lgkak5ozm7e4gdxxhk/K5EWy3Rfpg2Gfb5iivx4gamWG4I9ZyTRgcasXnG3U1yA5HApXgnIOu+H2HnJJnkbzTrfGMtFP4lff2Piyd8Ij+XQZkFO1qCo6EWl7uZ//Ol8svgt7smZjDwmIKRfc1gwQwUlD/OQ3lvEG+5KE6xwPuGqUBolPtG5Rija9rvqY2aVlhyjLuRSJhIYBozz2UOz4lZQ/zcVRlCDiR0MvU2+Vg680rkpCEkbiD4BLCCCO6raQx4wLGcEdIlY+DZeiqGNNJvcILn0DZ2sRO7x8z9D35A4RzNyrLs3ODVdnvOtKFDIxbJshO9Rk2kgd70OcWxiBH0VAtLWnN2xLS9eAoca8l1uhMGuqejt+5qGsLMySumToj2wS4TCN3xuyKvCD6MQlVhXCDGCifuCLoiSt/hbSfcxBXApQeoXBoOkIan2TXBQA=~-1~-1~1774087641~AAQAAAAF%2f%2f%2f%2f%2f%2fu%2fFONDyH98q468Thp8m0zwnqs2z%2ffkNEa3SQWR%2fb6k63Ery1Te4K0htStvVm65PTYlFS%2fEMWZlu%2fYN4pQV8I1bMKy9gOQze94S~-1; bm_sv=6C3B98B71C9CE3E6A7D1C70F1539E6DA~YAAQP7sbuIc2k/ecAQAA+R+nDx//2L87cm5nH5iwApwehlr5I2rNT1G4Sje66L4WBjRGFlonwJjdWYOjdXlsjZTHY0N3Ib4oQceLX5uTKlD3FmbG8gjr5UYuWfeio/fIyZ/dY03IaftIN1JYZZcjhY1xWA7GUA9ki/6zb+i9lwdBjIIyN5wRW0hLh7D5GHnWByoG628nvEQEc7sWvt7VsjiH/1Ea7EvVm72WXylwuahRSLXZOFGASjAPdk+QZl7yUY5qSQ==~1; ak_bmsc=0C57C38F214476EC5724885F3A84EF2B~000000000000000000000000000000~YAAQP7sbuCFKk/ecAQAAhVWpDx+XTnY0Ev4SePS26RIgdwWXWaPhHFoQBURuCf7cxKqn4UyRL0grmycjx+ZgcoZKG56y4nMDVSbBJ4mAcNVPaJW+6cQe1MM6rXUxRWPEFkyH6TdG4XSAOOeqT8eH5QWNJXIZ5/qlH+2aLNfOeTtoDhiJXGSW5FHDei16Qp8NhhIxm9NXyP8MBwG3218OEHT+ikN/RaTWqAU3eYsu02F5TZJu6/qDjcs6oEzigvWxfN1c0HGdlB8NgLuYBT6HWQOqFo6Z7Hqpp4+92r57ZMLoHmrdnPP0X3wao3V+CRfdGbbn2GohVhNnJNIdzOZITwT3lMuq51cvXXl04Rv7HqeV+VM8ZAIQn3ge74LUNlz0APHQWyae8Fbl0e6WLI+whIH3CxdLPRPw25oiEfgXQxdVNIRssuBs6H1noOligNmIbrOJh9MSRDh22t0UDxZWQaf3V/vupFbTlpt1WAzZ8znERg==; bm_s=YAAQ3MgsMSPu6vacAQAAMbKqDwUU7SEbr3mAE1wxRC5x07s3wfm1g5RRXjAxKA7ul9mnx8MOEorzxMfoTtwrfM7RZ6gNcbanwC7bC2BnSkbgY4JxFB8ZV5kEqVLaALvNLQyMY+DbmZ/se9DEa/WXlhvcaa1qTUY/kmY9EZhN+/R+essOy4O9gUL8IPSGbNQ0IeFArhGMPHI0LBcVouDc7/yYVxQivR3LYvSMQ+FZP62yPVtEt6bVsIOXbQ1FqitMgz7hc1d1+3nZWw6CrzYS7A6eFekqP33gme3EihYnpKxZhseWB6NQNndwnh0w4Mp9Wi00E5pKeTrJDyQbv+p8nlVgUODC6MFXMnscIYin7rICs5MjGRj4dSNW5ff47QU91sboo5NERVgW3lfQ9+zutqXh4MBOpJ5n14zrM1UDDMoP7c9P0YUfoTWv4o50DCmgr8DCsue0Gy/8FA3QmAsex6Ue75Zkxn3j42qTIRnD/+0HrSLWRvEYmoZRTbGlUyaziD6vVlRQCOhYK6OMNeVLahcqYA653roCjQsVOb78t10SAVb4cnvaYfBbAa+4B128bIwaMcQuEXvfh0XObQSQAurV9l52QuxZiAHgEREUfLIc1jw6F2ZwpTbrTHPlfROLXQ8+N8hV0O92aNiX5Yqarh7TauthXIfcfg5Pjo+M9BcVPSPQd8s3NaNMwRbmOTPQAKUzcdh8vbUXJ7gsp3JhIU9R0iR3km474ThgPsppuCJooTQ9MzmgmyowhE58TLZbA9M+Yav8fhnlU45XBPPQvtdr6s3PpVGHBI7xJdfDLA+8PgU3+4MuqNaHBnAlWPXPZRa2TZ8WRTLKsh5TW2MKDiPSmpUEpg3Nmn120OsNHtrCF8AYu6Z7VwGvGyROni44oMdtYxUaJfm4AHHGInMmEFf/XdRanfGUyPvaPPzAH2hAzX0wGpEHM4/aT91n0wNXPonU6HKKLpFfI3M4M1wMaDqMgUV/l3Eigzhbhe98VtM=; bm_so=6A2D4B588EB03D5C42D3A5A3D241F3BA3BC3A8B84E46C328612BDA99B50EED57~YAAQ3MgsMSTu6vacAQAAMbKqDwfd1AipB6jneU9ASlJRzGcTDdSwCh9aHfROTX4/KHC9tnHXQB80WuErRqyyTtMKQnvnb6P7ZHjCCkQ0fvCcJjOONHnzS+mSvRvgkbLE2kybXxgFUR0Dy0h9UKHgeYSmlMtbag0vMabgHqn3j4o0eDAA9M74JFpnvvf1hHRwL9uIi4jdeIDBzQz4/v1scjGloVuUZN9B6sXYtZmJhEs4v141QjbpYuGbZJKGcHxfKfXSgyXUpeEYu/QqmzxjkZAuzpeLQx1blg8reDip+3cZEUm+r3hOGVm+zdyp89bYcSYB34IxMpOybpgT/gdHsSSM3/9NzjzAAnZMbA8hCBp7QHWqQzewLDd3GZC5IZjxaedquQZ/72HyUAi6bPeYM4i3m1QS72ZkQ6rT/XFZTx/aL/3qtlSwmBwc/ySLQd+Zbcg/BZ7XmHi+IG4gbyZuwXwxkBuKhC0jv2dNzKiYNrph59vv/70MDU/5VA==; bm_sz=3CE76C988F6FC9A46430758783B59452~YAAQ3MgsMSXu6vacAQAAMbKqDx+MRSUyBEetALcMWK/x4ikdNkEw/wJP7p8nht7A0pK1UOTnAUj/cyiBUJ1LuBPivHVTq/5oUCVznbzLIxBO8N1pxsPfcBsdfykRlfUc2E7rlhtEvsypS0DjTDmHHTnIUy5tGIVzqJeqJF422NSjwqgmMDHwjd0tDpN2iEeAkg+L471LEn92BX/pLBiGFhTZT4GXXvxNN4YyvPNQ3UhfrozUf9+q6A5XtJ2Q61bIDuk0adULBw8fNZfZ5BjRnUCDryqsojn7ciOfoQJC233aixgbmb6c/7SVkijkZKI19yw14iKu/QxGb2A9YdjBpsYe1WoO7StGCEEu489pRV6ya9nyqRLArB2EWPSRp91/Y1BCRfn+2UsvfnLQNznzJPX+SAxSyXBzPSgvyn1bU0Sui6I8jwYChXQuyY7MgJ1RW/eAIVFqUnre42cMV1ZkksLaKeifxUxUi1yi2mRQZ1Ybw69XUvK0N61twwGpSIq65FvXVi5YXPjoj7MiKudry8f6Ywt4bWxWSg==~4339762~3162419; bm_lso=6A2D4B588EB03D5C42D3A5A3D241F3BA3BC3A8B84E46C328612BDA99B50EED57~YAAQ3MgsMSTu6vacAQAAMbKqDwfd1AipB6jneU9ASlJRzGcTDdSwCh9aHfROTX4/KHC9tnHXQB80WuErRqyyTtMKQnvnb6P7ZHjCCkQ0fvCcJjOONHnzS+mSvRvgkbLE2kybXxgFUR0Dy0h9UKHgeYSmlMtbag0vMabgHqn3j4o0eDAA9M74JFpnvvf1hHRwL9uIi4jdeIDBzQz4/v1scjGloVuUZN9B6sXYtZmJhEs4v141QjbpYuGbZJKGcHxfKfXSgyXUpeEYu/QqmzxjkZAuzpeLQx1blg8reDip+3cZEUm+r3hOGVm+zdyp89bYcSYB34IxMpOybpgT/gdHsSSM3/9NzjzAAnZMbA8hCBp7QHWqQzewLDd3GZC5IZjxaedquQZ/72HyUAi6bPeYM4i3m1QS72ZkQ6rT/XFZTx/aL/3qtlSwmBwc/ySLQd+Zbcg/BZ7XmHi+IG4gbyZuwXwxkBuKhC0jv2dNzKiYNrph59vv/70MDU/5VA==~1774084367026""".replace('\n', '').replace('\r', '')

# --- ANTI-BLOCK HEADERS ---
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Referer': 'https://www.sheinindia.in/sheinverse',
    'Origin': 'https://www.sheinindia.in',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Cookie': RAW_COOKIE
}

known_products = set()

# Session create karna taaki real browser jaisa lage aur block na ho
session = requests.Session()
session.headers.update(HEADERS)

def send_telegram_msg(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

def fetch_verse_data():
    global known_products
    try:
        response = session.get(API_URL, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            products = data.get('products', [])
            
            if not products:
                print("⚠️ Connected to Shein, but found 0 products. Cookie might be expired.")
                return False

            recent_products = products[:150]
            current_batch_ids = set()

            for item in recent_products:
                p_code = item.get('code')
                p_name = item.get('name', 'Product')
                p_url = f"https://www.sheinindia.in{item.get('url')}"
                
                current_batch_ids.add(p_code)

                # Naye item ka alert (Sirf tab jab purani list khali na ho)
                if p_code not in known_products and len(known_products) > 0:
                    msg = f"🔥 **NEW ITEM IN SHEINVERSE!**\n\n📝 {p_name}\n🔗 Link: {p_url}"
                    send_telegram_msg(msg)
            
            known_products = current_batch_ids
            return True

        elif response.status_code == 403:
            print("🚫 Blocked (403)! Shein caught the bot. Need a fresh Cookie.")
            return False
        else:
            print(f"⚠️ Error Code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 ADVANCED Shein Scanner Started (Anti-Block Active)...")
    send_telegram_msg("🚀 Advanced Verse Scanner Live! Tracking top 150 items. (Sleep: 30s)")
    
    # Pehla scan
    fetch_verse_data()
    
    while True:
        success = fetch_verse_data()
        if success:
            print(f"✅ Scanning complete. Tracking {len(known_products)} top items...")
        
        # 30 seconds rest as commanded
        time.sleep(30)
        
