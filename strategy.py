from config import BUY_THRESHOLD, SELL_THRESHOLD

class TradingStrategy:
    def should_buy(self, token):
        # Example logic: Buy if price has increased by more than the threshold
        if token['price_change_24h'] > BUY_THRESHOLD:
            return True
        return False

    def should_sell(self, token):
        # Example logic: Sell if price has decreased by more than the threshold
        if token['price_change_24h'] < -SELL_THRESHOLD:
            return True
        return False
