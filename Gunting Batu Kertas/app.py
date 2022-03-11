import random

# Gunting > Kertas
# Kertas > Batu
# Batu > Gunting
act = ["Gunting","Batu","Kertas"]

def enemy():
	desc = random.randint(0,2)
	enemy.enmy = act[desc]

def choose(pilih):
	if pilih == 1:
		choose.des = act[0]
	elif pilih == 2:
		choose.des = act[1]
	elif pilih ==3:
		choose.des = act[2]
enemy()
while True:
	print("================================")
	print("===1. Gunting")
	print("===2. Batu")
	print("===3. Kertas")
	print("================================")
	pilih = int(input("Masukan Pilihan -> "))
	choose(pilih)

	if enemy.enmy == "Gunting" and choose.des == "Kertas":
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("You Lose !!")
	elif enemy.enmy == "Kertas" and choose.des == "Batu":
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("You Lose !!")
	elif enemy.enmy == "Batu" and choose.des == "Gunting":
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("You Lose !!")
	elif choose.des == "Gunting" and enemy.enmy == "Kertas":
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("You Win !!")
	elif choose.des == "Kertas" and enemy.enmy == "Batu":
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("You Win !!")
	elif choose.des == "Batu" and enemy.enmy == "Gunting":
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("You Win!!")
	else:
		print("Pilihan Anda -> ",choose.des)
		print("Pilihan Musuh -> ",enemy.enmy)
		print("============================")
		print("DRAW !!! ")
