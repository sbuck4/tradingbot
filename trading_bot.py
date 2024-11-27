import requests

def get_solana_top_traded_tokens():
    url = "https://api.dexscreener.com/token-profiles/latest/v1"
    
    try:
        # Send a GET request to the Dexscreener API
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Filter for Solana tokens
            solana_tokens = [token for token in data if token.get("chainId") == "solana"]
            
            # Extract and return relevant details (chainId and Telegram name)
            result = []
            for token in solana_tokens:
                chain_id = token.get("chainId", "Unknown Chain")
                telegram_links = [
                    link.get("url") for link in token.get("links", []) if link.get("type") == "telegram"
                ]
                telegram_name = (
                    telegram_links[0].rsplit("/", 1)[-1] if telegram_links else "No Telegram"
                )
                result.append({"chainId": chain_id, "telegramName": telegram_name})
            
            return result
        else:
            print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
solana_tokens_with_telegram = get_solana_top_traded_tokens()

# Print the chainId and Telegram name in a clean format
print("Solana Tokens and Telegram Names:")
for token in solana_tokens_with_telegram:
    print(f"Chain ID: {token['chainId']}, Telegram Name: {token['telegramName']}")
