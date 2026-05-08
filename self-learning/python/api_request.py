import urllib.request
import json

def fetch_crypto_price(coin_id="bitcoin"):
    """Fetches real-time crypto prices using a public API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    
    print(f"Fetching current price for {coin_id}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                price = data.get(coin_id, {}).get('usd')
                if price:
                    print(f"Current {coin_id.capitalize()} Price: ${price:,.2f}")
                else:
                    print("Price data not found in response.")
            else:
                print(f"Failed to fetch data. HTTP Status: {response.status}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_crypto_price("bitcoin")
    fetch_crypto_price("ethereum")
