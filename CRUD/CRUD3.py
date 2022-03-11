import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="shoppingyuk"
	)

if db.is_connected():
	print("Berhasil terhubung")

print("====================================")
print("1. Insert Data")
print("2. Tampil Data")
print("3. Hapus Data")
print("4. Update Data")
print("99. Exit")
print("====================================")

while True:
	pilih = input("Masukan pilihan -> ")

	if pilih == "1":
		kode = input('Masukan Kode Pelanggan -> PLG-XXX ->')
		nama = input('Masukan Nama Pelanggan -> ')
		alamat = input('Masukan Alamat Pelanggan -> ')
		telp = input('Masukan nomor hp pelanggan -> ')


		cursor = db.cursor()
		sql = "INSERT INTO pelanggan (kd_pelanggan,nama_pelanggan,alamat_pelanggan,telp_pelanggan) VALUES (%s,%s,%s,%s)"
		val = (kode,nama,alamat,telp)
		cursor.execute(sql,val)

		db.commit()

		print("{} data ditambahkan".format(cursor.rowcount))


	elif pilih == "2":
		cursor = db.cursor()
		sql = "SELECT * FROM pelanggan"
		cursor.execute(sql)

		results = cursor.fetchall()

		for data in results:
			print(data)

	elif pilih == "3":
		cursor = db.cursor()
		sql1 = "SELECT * FROM pelanggan"
		cursor.execute(sql1)

		results = cursor.fetchall()

		for data in results:
			print(data)

		kd_hapus = input('Masukan Kode yang ingin dihapus -> ')

		sql2 = "DELETE FROM pelanggan where kd_pelanggan=%s"
		val = (kd_hapus,)

		cursor.execute(sql2,val)

		db.commit()

		print("{}data dihapus".format(cursor.rowcount))
	elif pilih == "4":
		cursor = db.cursor()
		sql1 = "SELECT * FROM pelanggan"
		cursor.execute(sql1)

		results = cursor.fetchall()
		for data in results:
			print(data)
		kd_update = input("Pilih data yang ingin diganti -> ")
		nm = input("Masukan nama baru -> ")
		almt = input("Masukan alamat baru -> ")
		telp = input("Masukan telp baru -> ")

		sql2 = "UPDATE pelanggan SET nama_pelanggan=%s,alamat_pelanggan=%s,telp_pelanggan=%s WHERE kd_pelanggan=%s"
		val = (nm,almt,telp,kd_update)
		cursor.execute(sql2,val)

		db.commit()
		print("{}data berhasil dirubah".format(cursor.rowcount))
	elif pilih == "99":
		exit()