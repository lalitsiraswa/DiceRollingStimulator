# Generating random numbers
import random

print("This is a Dice Stimulator")

enter = 'y'
while(enter == 'y'):
	number = random.randint(1, 7)
	if(number == 1):
		print("[-----------]")
		print("[           ]")
		print("[     O     ]")
		print("[           ]")
		print("[-----------]")
	elif(number == 2):
		print("[-----------]")
		print("[           ]")
		print("[  O     O  ]")
		print("[           ]")
		print("[-----------]")
	elif(number == 3):
		print("[-----------]")
		print("[     O     ]")
		print("[     O     ]")
		print("[     O     ]")
		print("[-----------]")
	elif(number == 4):
		print("[-----------]")
		print("[  O     O  ]")
		print("[           ]")
		print("[  O     O  ]")
		print("[-----------]")
	elif(number == 5):
		print("[-----------]")
		print("[  O     O  ]")
		print("[     O     ]")
		print("[  O     O  ]")
		print("[-----------]")
	elif(number == 6):
		print("[-----------]")
		print("[  O     O  ]")
		print("[  O     O  ]")
		print("[  O     O  ]")
		print("[-----------]")
	enter = input("Press 'y' for roll again or 'n' for stop rolling : ")








# import datetime

# print(type(datetime)) # module
# print(type(datetime.datetime)) # class

# object = datetime.datetime(2020, 8, 31)
# print(type(object)) # object
# for i in range(5):
# 	for j in range(13):
# 		if(j == 12):
# 			print("]", end="")
# 		elif(j == 0):
# 			print("[", end="")
# 		elif(i == 0 or i == 4):
# 			print("-", end="")
# 		else:
# 			print(" ", end="")
# 	print("\n", end="")
