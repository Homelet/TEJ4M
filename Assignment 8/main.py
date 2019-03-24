def chicken_with_rabbit_cage(heads, legs):
	chicken = 0
	while chicken < heads:
		rabbit = heads - chicken
		if rabbit * 4 + chicken * 2 == legs:
			return chicken, rabbit
		chicken += 1
	return None


result = chicken_with_rabbit_cage(heads=35, legs=94)

if result is None:
	print("No Result")
else:
	print("Chicken: {}\nRabbit {}".format(result[0], result[1]))
