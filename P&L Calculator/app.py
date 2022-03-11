def proloss(buy,sell):
	if buy > sell:
		#loss
		loss = 1 - (sell/buy)
		xl = buy - sell
		if xl <= buy:
			print("Kamu Loss -> -","{:.0%}".format(loss),"atau $",xl)
	elif buy < sell:
		#profit
		profit = 1 - (sell / buy)
		xp = sell - buy
		if xp >= buy:
			print("Kamu Profit -> ","{:.0%}".format(profit),"atau $",xp)


buy = float(input("Harga Beli : "))
sell = float(input("Harga Jual : "))

proloss(buy,sell)