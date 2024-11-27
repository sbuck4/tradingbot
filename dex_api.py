import requests

API_URL = "https://api.dexscreener.com/latest/dex/tokens"

def fetch_token_profiles():
    url = 'https://api.dexscreener.com/latest/tokens'  # Use the correct endpoint
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return {}

    data = response.json()

    # Log full response for debugging
    print("Full response from Dexscreener API:", data)

    # Ensure that pairs exist in the response
    if 'pairs' not in data or not data['pairs']:
        print("No token pairs data available.")
        return {}

    return data

def fetch_token_boosts():
    """Fetch token boosts from Dexscreener."""
    response = requests.get(f"{API_URL}/boosts")
    if response.status_code == 200:
        return response.json()
    return []

# Define or correct this function if it is missing
def get_token_by_address(chain_id, token_address):
    """Fetch token details by address from Dexscreener."""
    response = requests.get(f"{API_URL}/token/{chain_id}/{token_address}")
    if response.status_code == 200:
        return response.json()
    return None

def get_top_tokens():
    # Fetch token profiles
    token_profiles = fetch_token_profiles()

    # Print the raw response for debugging
    print("Raw token profiles response:", token_profiles)

    # Check if we received valid data
    if not token_profiles or 'pairs' not in token_profiles or not token_profiles['pairs']:
        print("No token data available.")
        return [], []

    pairs = token_profiles['pairs']

    # Sort tokens by trading volume (volume_24h) and liquidity
    sorted_by_volume = sorted(pairs, key=lambda x: x.get('volume_24h', 0), reverse=True)
    sorted_by_liquidity = sorted(pairs, key=lambda x: x.get('liquidity', 0), reverse=True)

    # Get the top 10 most traded and most liquid
    top_10_traded = sorted_by_volume[:10]
    top_10_liquid = sorted_by_liquidity[:10]

    return top_10_traded, top_10_liquid
