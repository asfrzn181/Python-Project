from MyQR import myqr
import tkinter as tk
from urllib.request import urlopen
from lxml.html import parse



def KodeQR():
    url = link.get()
    #urllib request for get url title
    page = urlopen(url)
    x = str(parse(page).find(".//title").text)
    myqr.run(url, save_name = 'QR_'+x+'.png')

box = tk.Tk()
box.geometry("600x200")
box.config(bg="#EC7063")
box.resizable(width=False, height=False)
box.title('QR Code Generator')

link = tk.StringVar()
tk.Label(box,text = 'QR CODE GENERATOR ', font ='arial 20 bold',fg="White",bg="Black").pack()

tk.Label(box,text = 'Masukkan URL : ',font = 'arial 20',fg="Black",bg="#EC7063").place(x=5, y=60)
tk.Entry(box, width=53,textvariable = link,font='arial 15 bold',bg="lightgreen").place(x = 5, y=100)
tk.Button(box,text = 'GENERATE', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=KodeQR).place(x=385 ,y = 140)

box.mainloop()
