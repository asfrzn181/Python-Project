import datetime
from forex_python.converter import CurrencyRates
from tkinter import *

root = Tk()
root.geometry("300x200")

#Var
start = datetime.datetime(2022,1,29)
x = datetime.datetime.now()
times = x - start
time = times.days
money = 10
i = 1
#END VAR


con = CurrencyRates().get_rate('USD','IDR')
data = Listbox(root,height=200,width=200)
data.place(x=0,y=0)
bunga = money*con
while i <= time:
	if i != time:
		res = round(money,2)*0.02
		money = round(money,2)+res
		rupiah = money*con
		tod = round(rupiah,0)
		fix = "{:,}".format(tod)
		data.insert(0,"Hari ke -> "+ str(i) + " -> $"+str(round(money,2)) + "-> Rp."+str(fix))
	else:
		rupiah = money*con
		tod = round(rupiah,0)
		fix = "{:,}".format(tod)
		data.insert(0,"____________________________________________________")

		data.insert(0,"Rate USD -> IDR = " + str(con) + "*realtime*")
		data.insert(0,"BUNGA/day-> 2%")
		data.insert(0,"Fix yang harus dibayar dalam rupiah -> Rp." + str(fix))
	i += 1
bun = rupiah - bunga
bung = "{:,}".format(bun)
print("Bunga yang didapatkan adalah -> Rp." + str(bung)  )


root.mainloop()