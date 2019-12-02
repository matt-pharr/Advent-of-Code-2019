totalfuel = 0
with open("input.txt") as masses:
	for line in masses:
		val1 = int(line)//3-2
		totalfuel += val1
		while val1 > 0:
			val1 = val1//3 - 2
			if val1 > 0:
				totalfuel += val1
print(totalfuel)