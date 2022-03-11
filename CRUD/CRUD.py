import mysql.connector
from tkinter import *
from tkinter import messagebox
#koneksi START
db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="shoppingyuk"
	)

if db.is_connected():
	print("Berhasil terhubung")


cursor = db.cursor()
#koneksi END
#Automatis Kode Pelanggan
terakhir = "SELECT * FROM pelanggan"
cursor.execute(terakhir)
cursor.fetchall()
y = cursor.rowcount
if y > 0:
	terakhir = "SELECT max(substr(kd_pelanggan,-2))+1 as kode FROM pelanggan"
	cursor.execute(terakhir)
	x = str(cursor.fetchall())

	y = x.replace("[(","")
	code = y.replace(".0,)]","")

	if cursor.rowcount <= 9 :
		newCode = "PLG-00" + code
	elif cursor.rowcount < 1000:
		newCode = "PLG-0" + code
else:
	newCode = "PLG-001"

#End Kode Pelanggan Auto
root = Tk()

root.geometry("600x500")
root.title('Form Insert Data')

label_0 = Label(root,text="Form Insert Data", width=20, font=("bold",20))
label_0.place(x=90,y=60)

label_1 = Label(root,text="Kode PLG",width=20,font=("bold",10))
label_1.place(x=80,y=130)


txtkdplg= Entry(root)
txtkdplg.place(x=240,y=130)
txtkdplg.insert(0,newCode)
txtkdplg.config(state='disabled')

label_2 = Label(root,text="Nama Pelanggan",width=20,font=("bold",10))
label_2.place(x=68,y=180)

txtnmplg=Entry(root)
txtnmplg.place(x=240,y=180)

label_2 = Label(root,text="Alamat Pelanggan",width=20,font=("bold",10))
label_2.place(x=70,y=230)

txtalamatplg=Entry(root)
txtalamatplg.place(x=240,y=230)

label_3 = Label(root,text="Telp Pelanggan",width=20,font=("bold",10))
label_3.place(x=72,y=280)

txttelpplg=Entry(root)
txttelpplg.place(x=240,y=280)

xsql = "SELECT kd_pelanggan FROM pelanggan"
cursor.execute(xsql)
res = cursor.fetchall()



tmpldata = Listbox(root,height=5,width=50)
tmpldata.place(x=120,y=330)

for data in res:
	tmpldata.insert(0,*data)

def clear():
	txtnmplg.delete(0,END)
	txtalamatplg.delete(0,END)
	txttelpplg.delete(0,END)
	txtkdplg.focus_set()



def insert():
	kdplg = txtkdplg.get()
	nmplg = txtnmplg.get()
	almtplg = txtalamatplg.get()
	telpplg = txttelpplg.get()
	cursor = db.cursor()
	sql = "INSERT INTO pelanggan (kd_pelanggan,nama_pelanggan,alamat_pelanggan,telp_pelanggan) VALUES (%s,%s,%s,%s)"
	val = (kdplg,nmplg,almtplg,telpplg)

	x = cursor.execute(sql,val)
	
	tmpldata.after(0,)
	messagebox.showinfo("showinfo","Tersimpan")
	clear()
	db.commit()


Button(root,text='Insert',width=20,bg="black",fg='white',command=insert).place(x=120,y=440)
Button(root,text='Clear',width=20,bg="black",fg='white',command=clear).place(x=280,y=440)


root.mainloop()