from trading_bot import get_top_tokens

def main():
    # Get top tokens (traded, liquid, and boosted)
    top_10_traded, top_10_liquid, top_10_boosted = get_top_tokens()

    # Output the top 10 most traded tokens
    print("Top 10 Most Traded Tokens in the Last 24 Hours:")
    if top_10_traded:
        for token in top_10_traded:
            print(f"Name: {token.get('name', 'Unnamed Token')}, Volume (24h): {token.get('volume_24h', 'N/A')}")
    else:
        print("No data available for traded tokens.")

    # Output the top 10 most liquid tokens
    print("\nTop 10 Most Liquid Tokens:")
    if top_10_liquid:
        for token in top_10_liquid:
            print(f"Name: {token.get('name', 'Unnamed Token')}, Liquidity: {token.get('liquidity', 'N/A')}")
    else:
        print("No data available for liquid tokens.")

    # Output the top 10 most boosted tokens
    print("\nTop 10 Most Boosted Tokens:")
    if top_10_boosted:
        for token in top_10_boosted:
            print(f"Name: {token.get('name', 'Unnamed Token')}, Boost Percentage: {token.get('boost_percentage', 'N/A')}")
    else:
        print("No data available for boosted tokens.")

if __name__ == "__main__":
    main()
