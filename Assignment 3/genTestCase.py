import random


name = "test_6"
target = 15

with open(name + "_x", "w") as f:
	for i in range(0, target):
		f.write(str(random.random()) + "\n")

with open(name + "_y", "w") as f:
	for i in range(0, target):
		f.write(str(random.random()) + "\n")
