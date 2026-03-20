import time
import random
import requests

# --- CONFIGURATION (COMPLETED) ---
TOKEN = "8743319750:AAE6To6hX2b2gzG2PBTmfQDt1jPYGcqUdWI"
CHAT_ID = "6814671965"

# Aapki provide ki hui Final Cookie
COOKIE_STR = """V=1; _gcl_au=1.1.1503199170.1773918704; _fbp=fb.1.1773918703871.453933530924856478; _fpuuid=AqmDvQ8BXiwNFBIipm0ap; deviceId=AqmDvQ8BXiwNFBIipm0ap; EI=mcqJQvYOa0UyB7gpill1of8U6vpbLKn1clO%2BOcZuDmLBGnmQsymHC8huZb2WDcEQ; mE=she***************%40gmail.com; mN=91XXXXX560; un=aditya%20; MN=9198308560; CI=eb45c64f-699e-4ab7-87c0-712ad6df934f; PK=2O9VKB0%2B%2BKGPGSCWCnKwqWleYJP94kolBaFF8jQqrpLVFyTNSPJL4LAcaOQy5%2B31; SN=aditya; G=M; A=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJzaGVpbl9hZGl0eWFyYW9yYmpAZ21haWwuY29tIiwicGtJZCI6ImViNDVjNjRmLTY5OWUtNGFiNy04N2MwLTcxMmFkNmRmOTM0ZiIsImNsaWVudE5hbWUiOiJ3ZWJfY2xpZW50Iiwicm9sZXMiOlt7Im5hbWUiOiJST0xFX0NVU1RPTUVSR1JPVVAifV0sIm1vYmlsZSI6IjkxOTgzMDg1NjAiLCJ0ZW5hbnRJZCI6IlNIRUlOIiwiZXhwIjoxNzc2MDEyMDMwLCJ1dWlkIjoiZWI0NWM2NGYtNjk5ZS00YWI3LTg3YzAtNzEyYWQ2ZGY5MzRmIiwiaWF0IjoxNzczNDIwMDMwLCJlbWFpbCI6ImFkaXR5YXJhb3JiakBnbWFpbC5jb20ifQ.U7yf-GMwLIXB9sZjNcixEhevk0YirrELcYJEICxNqusv3bdNY74GkKhtAPLXC5dL9MMfkPB7L_yqhCBkqyzk-oaA6eCya7K0Z1VrZY4usMusxIr_I9o0Bb3PqHjfw7mVudgCJNRveV-On45OEPg4Oj45gw-0xCWINWEfDJ08dnVMf9HbYnJqAepYbapeL1IH8YZ6gQCsmc0JFgWb6HbF3OkZ5f-HD_pu_TykBCPXAF0AvrELATteoD0EoRKy5vwCa_vinabKGg5RScTIrbc1U7I1zIvPEEz62g4SMnvoSTBJ3S9LUI2HCa5BlyljpjVnnr36UZvUySAn-XgMITubaw; U=adityaraorbj%40gmail.com; LS=LOGGED_IN; R=eyJhbGciOiJSUzI1NiJ9.eyJzZXNzaW9uIjp7InNlc3Npb25JZCI6ImYyYjIwMzEwLTU4MWUtNDAxYi05OTA5LTg1N2RhMWU3Y2I3NiIsImNsaWVudE5hbWUiOiJ3ZWJfY2xpZW50Iiwicm9sZXMiOlt7Im5hbWUiOiJST0xFX0NVU1RPTUVSR1JPVVAifV19LCJ0eXBlIjoicmVmcmVzaCIsInRlbmFudElkIjoiU0hFSU4iLCJzdWIiOiJzaGVpbl9hZGl0eWFyYW9yYmpAZ21haWwuY29tIiwiZXhwIjoxNzg4OTcyMDMwLCJpYXQiOjE3NzM0MjAwMzB9.dWHJzJycwCEF_sQwcfygrBd31rVrerLvxAP9-E2sa_bWENNI3To3fmA3lvOhHhDwdtPFvoxpeoS6a-8WVG8LjIXAB5C6qIC9nVIYE2iVhireyTUI3251-hJjm5hk_pEsQOklQKIsrKgm8F0CCppdISaW2lNUD6WC6lO8-Z5Z7HYQzF1F1JV4tEtYSc3ncf5jtWOWkpwz8J4cD1Sox52ndCRKUqgp7J4Jgyh-Xt4V5M1WHbUrsJIICai7Cpwl2g3Y_Dp-EDMDmuyrwFNbJCnaNuB4UBiSU1tiyzF6DjOIGwxZiwE326AxO5aNzIhORLcpwBVTJw4E3lJoTC6dPQv9Dw; M=SH9237708413; GUID=18f80a8b-972e-42e2-925a-a6ca4e080dd7; C=SH9237708413; customerType=Existing; cohortSegment=17,19,10; jioAdsFeatureVariant=true; storeTypes=shein; recentlyViewed=[{"id":"443327888_green","store":0},{"id":"443391939_pink","store":0},{"id":"443388638_beige","store":0},{"id":"443387232_lightblue","store":0},{"id":"443331909_green","store":0}]; bookingType=SHEIN; _gid=GA1.2.1478552207.1774027562; _ga_F1NJ1E2HJ2=GS2.1.s1774027586$o1$g0$t1774027586$j60$l0$h0; sessionId=sess_1774027597805_tvcwj3rv6; CT=ALLAHABAD; ST=UTTAR PRADESH; ZN=undefined; PG=; bm_ss=ab8e18ef4e; _gac_G-D6SVDYBNVW=1.1774034815.Cj0KCQjw4PPNBhD8ARIsAMo-icwE7fkWF2OmnI-QHa3Di0HaL61wlxU050MY-cOIGcQ9pTnDNrh2jDsaAjKoEALw_wcB; ak_bmsc=D8580895322A712D466D56EA14710C97~000000000000000000000000000000~YAAQP7sbuNFtf/ecAQAA2Q63DB/jrezV97xmcl6vMmxmzkEKOGnWv58yA/xUgxBo6ncjo7V3B1Mat7iCKIqXs7l9ZkPFPh1TQcN9NnuLOzQCRD6VV0UmB8RGFkO/4n/vu+PpWzRwHhX2m5PrYs/C6z9mc+Up9nr9t2VUwfBD/v9YYv3mq6rUenKfeZLMvHlj/f91v7ovFhn5Jkr4V2T9N++xyS41YrKsuHftkq+598kV+NwrExiowERuE4PuLTvqr/CXbJ4Mxh2yBi2ZvtabFfz6uBG+ssZgHbCc7CCORzVW5HDnQ7EWi9EkjiCp+qUG35dySB+JLJLjaMxIKFMYQNaNH0kSOsJlvC2hxY+MAh012LHewZ4mEx0LsepjF8JtufdPdUJlMNTj4sCWrEQf7PNMuxMbNgmqPn9mW5S5UpBa1XIv5CnW4sLi20Qgfd9PvjBERPbbeMA/3KK0slNB65MvaJfaRik1zK0IeV2aMC8+cfY=; customerType=Existing; _gcl_gs=2.1.k1$i1774034810$u6234225; _abck=58B8F7AB81B70722B3B58265D253A919~0~YAAQniHKFyxBygqdAQAAt/jgDA+24EV48vUA2IF7ksmf2cyH+XLJKVmUfMLCV1+1WF/3qT2E7pBwuFmULDvdJvudCgpqXu47FanJRmLqqjJeHal8Nud/h5dRBXPbom6GFyTfD2oEXpBk7bOgYHydZ4z9CKrxx4Y8Vq66ch/1qoFFbgoItwStdUGhR3T2JHbsdgeggzMMtvw7I8vU4sd6mgjuu8K0ARpwj8KUPiQnwIdc+nrwBm0sBesvVrbM+xVcEcF7z61yHZU4PYCHNfuVU3qHXcm4HOQQmLWHVDAygSFbIdvYuoGJYKxm3qac5w1d3vt4oFslueSWOdmin+FNLAVUkn5CuyN56WmGnGAT2WN1jNjo+AgEMC01hDRob63ca+l0bDa6ljoTwhw9gI2GE67upK0bUGozBN6oyp9Nv7UcLtYT/Iv7s8KdZJAp2zcbbuCt88+pESm9RwP6Lx6ufTxopWJmWIJBnAA5DYRpsC1WGH/oj7mUT1856yUdjYNHUDhNRm+vqP7gDkXvX4oPFA6ucI6F320O1XI75kfgzUTqkHYkO0RdMvJZ/HLMjJEwY9HK2Ap+FVfJX7jvtFTOEBOoH7c+DRVlyy/P4u0rmnB0L5b1AU19bHxdFbR0mvA6ttyrqn6/siE6zJq4gtEj8G0imj1ccCNA/bIRHBvQzuieLBq+omcwXlD7QEZBv2X5t86eTbNirUwfByK+1pKZ+2bDf8m9gVcVpb2s4nDM9ZDIa3GkG+oQRxDWZHkXzQAAdGP+oDZ0kr/Lv/+pTLxpNcIN8v0hcBX8rC0IQlHP5ikc3qw/EQdLAuroCJzUi/QrYltZsP9v115MkZdjRa5MOtqc/5DJ9qM8xqu/XqiknHKZ5wK6lYbdapGGZUkC5sMWX1yrzxo1MR87m8U6INhzxNnl2BBtockLbxvm7XRKJrpbeIaWTn9EWPDjqcQLlpw=~-1~-1~1774038415~AAQAAAAF%2f%2f%2f%2f%2f3q+xms5VxptrJqm1lmBHnnOlV6IwCkxgNLUiWZFFYDV1sTQrLXvmQNI7yZbAWAOvDPWqV+knw7R6CZ3GgQB55EY%2fUzxSbByRuCfRR3SWZLJKErHUx7zLNKiFoI3IoNVpMufeYQ%3d~-1; bm_so=3BDAEFD58230B2F3ABAE6EF7BE6FC9C528AA0D741E451697D86C3BA51CC8AE91~YAAQniHKFy5BygqdAQAAt/jgDAc3dsgbP/QAMB7v15A6GnwaRIBw3jovkZIMZ6UF/w8W4VbqAtGpK345RCPu8So0Cf6DajaxDhnP9A8sdaU4N6I8NZ5aFJeo4A77NwCPyfAlERZJxasBMbE+xzpbXpgVmLxXoM8QacT+0sFth+t9b9LV6VJpXdWwSWaNs9O9JbP/1Ht5pEzzh+s5qjRDbYrlbto7Rg9qH+cdibrHWEKthGfu8p3GDTyn2tggj8KsY9SHvfAVjqAjUUo/rEYJ0DP4nkDHc/ax0gomUHLeRayNC4afk5OeVUEQCh8wRO+zvC9ZQ2mH1QmG+AFFbVKweab5ZXSeiI28obRD7+iFpbSMiufAzNhIojg5gLlN3SuRwjQ00qIOjcciKO+Ts86qmPYQTgpA46YzmYG8PsSoTCxDtL2b01qMrRNhwJzDJP3slaPm7pMPoesj67XhikDkLbsk=; bm_s=YAAQniHKF69BygqdAQAAYw/hDAXNmku0A+PE0FgDyOwKH1PfwyeX5p6Neduuh2b6XRfg7ScO8oY2jw08i0EH/IzuJXjDuCg6iRqg2ir4P4l3NagadHfI9Fr5izsETanCF+GTs8r0UF/vGOOKYWewySGTj5iw9UmnXrtzoxULx/aiCZiJfY7AOLoYnlo5szXrAOEOScSe0zJZe4cvCgEHKn4HnjNPDpbGQwvUU+XyCXZOSdFYGMRGCIW86yj8FpivhtI9G1SWhpxTeEVca0ZsE7kza77C0tF4hsu/ykKFOixewbE62/lf+I0yHkdTZ8oX07CYIH450rUgcdFBhm+hPKR8Zn9WLtFqqf1fjxRqqIB5gfxOhJ1hIbXiMAwTQVyM06cP/7cWB84tZw1r0PTy1bxuODOo9xuWGJvbZEvXY/snydJ8R7hNepVOAb3jm9tZ5xVH8FQ1qhzjGkqDalMmMIJiwIjukhFC/85LZ01dbegy4LNVJu3V4XssWrdrB4eJ/gvt5QXdRgQsS0U6Gqr0CVYuXqwKhxsXVfRAJsg5KbcOYE3ulVa2WYyUuBGhMsDCcSejvEIvJVDHiXXz1xnTyB8WsgTXWTSOs3vmcsXU9g0dTXHyy5v2iDX/BYW7TnTgLWeOBnjqITlBejWoThIOmB3QPHYEvQbv69L3S3GQhwkH6iIruUqx5DybuIUkN/Z5uYZit+w+5c94+b1hLC9eGtcaiotHxIiUpaJQQyg0GRMVpMiFNX084K6ohpUli5rNfN+BimHqcsoJVireCSJHMOpE0ZMFRD+1XVuEZeCfABrbcPH1wOb/RJRSry/Fw1+8KQa6+wHO2zn+iYifHDaVfW81TktmqmZsutclLNSZeIyDiWTy+3AN/N8+77IjGkdt7TV4WJX3ON6DSyiX9txl4cItki5iXJ6fCGHz5qlgfUt3Tpresui4yRooedkV05QFyVwK1gRhEd37IA==; bm_sz=E90109D1519722015412C7BEE841DBD2~YAAQniHKF7FBygqdAQAAYw/hDB9rYzvYPoKgGxEuTGDIu4PNKV5Dh8HmAoOx9ByK1w3TgkmWWZiKpPynqzu9mG/8aXkejgbQgEcgGRe2I0D3pKJRUfZv12rf8xxUXLEhRSdrxBPFhiHGMGXu4xk3zpvnNlijRWQ4dxZtkoXdYr0PwP3QE56sxMnCpuvqvQDHQVNA9a3tNekNqYcvRLuagDxPcgFAsQFaOYdo36iwV9sQyo2y3G1p5ThbJKo03Dc2SZfEldEu7Y6j3ivFsY6/EeWVZJBwy37WnFdiN3x9P0cmvV5JFaA+tfiQkM8nNpqCUhnSS9ek46DLGakZlHGCgmY9kZsGDdpCbedDSt5XBJQSQbuszgtgzfhgt6wtw0j5SUeH++E8WnU2MWbRXt6YcgiRfNSNJWk3rJ8apxQqzEj2J8y7I++/W0jOfYWo2mopBycneoAI+zSrQp7qXP2Vo+FwunZCTWNJkiMUCd2U6KMpwo7z8Gkzl8vAUhMomnFXds8qXv3fz5YabN133kVVjwmyQ5atgDwu~3748933~3487029; bm_sv=02E6A986B065A1303EACE9ED0272A381~YAAQniHKF9BBygqdAQAATBbhDB+tvR6Jt9na6as8C6VWx6HDQPK/j+o3pclJxglnchBh0knXw8a8k0MEKNiQ3H9p3kZwmR9qtcQSYXcpSJ/poFErwhpE9l0jN7dD7J7/QEQgYQ2eZzEIdzJMYIX9vXv++vl4DspDnHC51f9ivhU1uAGn43XCTlZspsX0tqoA7gqiW8P3ZBe97+WUtFf7ULnpaWIJoCJg5TLnUH0aB2hinqNppIvzkv09AMBmCJ4VjYZ5qQ==~1; _gcl_aw=GCL.1774037574.Cj0KCQjw4PPNBhD8ARIsAMo-icwE7fkWF2OmnI-QHa3Di0HaL61wlxU050MY-cOIGcQ9pTnDNrh2jDsaAjKoEALw_wcB; _ga=GA1.1.176576588.1773918703; bm_lso=3BDAEFD58230B2F3ABAE6EF7BE6FC9C528AA0D741E451697D86C3BA51CC8AE91~YAAQniHKFy5BygqdAQAAt/jgDAc3dsgbP/QAMB7v15A6GnwaRIBw3jovkZIMZ6UF/w8W4VbqAtGpK345RCPu8So0Cf6DajaxDhnP9A8sdaU4N6I8NZ5aFJeo4A77NwCPyfAlERZJxasBMbE+xzpbXpgVmLxXoM8QacT+0sFth+t9b9LV6VJpXdWwSWaNs9O9JbP/1Ht5pEzzh+s5qjRDbYrlbto7Rg9qH+cdibrHWEKthGfu8p3GDTyn2tggj8KsY9SHvfAVjqAjUUo/rEYJ0DP4nkDHc/ax0gomUHLeRayNC4afk5OeVUEQCh8wRO+zvC9ZQ2mH1QmG+AFFbVKweab5ZXSeiI28obRD7+iFpbSMiufAzNhIojg5gLlN3SuRwjQ0qIOjcciKO+Ts86qmPYQTgpA46YzmYG8PsSoTCxDtL2b01qMrRNhwJzDJP3slaPm7pMPoesj67XhikDkLbsk=~1774037577187; _ga_D6SVDYBNVW=GS2.1.s1774037560$o6$g1$t1774037612$j8$l0$h735614410"""
# ---------------------------------

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
]

notified_products = set()

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Telegram Error: {e}")

def check_wishlist():
    url = "https://www.sheinindia.in/api/wishlist/getwishlist?currentPage=1&pageSize=100"
    
    clean_cookie = COOKIE_STR.strip()
    bearer_token = ""
    if "A=" in clean_cookie:
        bearer_token = clean_cookie.split("A=")[1].split(";")[0]

    headers = {
        'authority': 'www.sheinindia.in',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {bearer_token}',
        'user-agent': random.choice(USER_AGENTS),
        'referer': 'https://www.sheinindia.in/wishlist',
        'cookie': clean_cookie
    }

    try:
        print(f"[{time.strftime('%H:%M:%S')}] 🕵️ Scanning Wishlist...")
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('info', {}).get('products', []) or data.get('info', {}).get('goodsList', [])
                
            print(f"✅ Success! Found {len(items)} items.")
            
            for item in items:
                goods_id = str(item.get('goods_id', ''))
                is_out_of_stock = item.get('isOutOfStock', False) or str(item.get('stock', '1')) == '0'
                
                if not is_out_of_stock:
                    if goods_id not in notified_products:
                        name = item.get('goods_name', 'SHEIN Product')
                        price = item.get('retailPrice', {}).get('amountWithSymbol', 'N/A')
                        size = item.get('attrSize', 'N/A')
                        link = f"https://www.sheinindia.in/product-p-{goods_id}.html"
                        
                        msg = (
                            f"🔥 <b>SHEIN RESTOCK ALERT!</b> 🔥\n\n"
                            f"🛍 <b>Item:</b> {name}\n"
                            f"💰 <b>Price:</b> {price}\n"
                            f"📏 <b>Size:</b> {size}\n\n"
                            f"🛒 <a href='{link}'>👉 CLICK HERE TO BUY NOW</a>"
                        )
                        send_telegram(msg)
                        notified_products.add(goods_id)
                        print(f"🔔 Notification sent for {goods_id}")
        else:
            print(f"❌ Error {response.status_code}. SHEIN block kar raha hai.")
            
    except Exception as e:
        print(f"⚠️ Network Error: {e}")

if __name__ == "__main__":
    print("🔥 SHEIN Bot Active!")
    send_telegram("🚀 <b>Bot Active on Railway!</b>\nAapki wishlist scan ho rahi hai.")
    while True:
        check_wishlist()
        time.sleep(random.randint(120, 240))
        
