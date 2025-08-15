def sean_strat(price, future_price):
	if price > future_price:
		return "Sell"
	elif price < future_price:
		return "Buy"
