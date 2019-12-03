with open("input3.txt") as inputfile:
	blabla = inputfile.read().split()
	inputlist1 = blabla[0].split(",")
	inputlist2 = blabla[1].split(",")

def intersections(inputlist1, inputlist2):
	input1 = set()
	input2 = set()
	pos = [0,0]
	steps1 = 0
	length1 = {}
	for direction in inputlist1:
		if direction[0] == "U":
			for i in range(int(direction[1:])):
				steps1 +=1
				#print(direction[1:])
				input1.add((pos[0], pos[1]+i+1))
				length1[(pos[0], pos[1]+i+1)] = steps1
			pos[1] = pos[1] + int(direction[1:])
		if direction[0] == "D":
			for i in range(int(direction[1:])):
				steps1 +=1
				#print(direction[1:])
				input1.add((pos[0], pos[1]-i-1))
				length1[(pos[0], pos[1]-i-1)] = steps1
			pos[1] = pos[1] - int(direction[1:])
		if direction[0] == "R":
			for i in range(int(direction[1:])):
				steps1 +=1
				#print(direction[1:])
				input1.add((pos[0]+i+1, pos[1]))
				length1[(pos[0]+i+1, pos[1])] = steps1
			pos[0] = pos[0] + int(direction[1:])
		if direction[0] == "L":
			for i in range(int(direction[1:])):
				steps1 +=1
				#print(direction[1:])
				input1.add((pos[0]-i-1, pos[1]))
				length1[(pos[0]-i-1, pos[1])] = steps1
			pos[0] = pos[0] - int(direction[1:])


	pos = [0,0]
	steps2 = 0
	length2 = {}
	for direction in inputlist2:
		if direction[0] == "U":
			for i in range(int(direction[1:])):
				steps2 +=1
				#print(direction[1:])
				input2.add((pos[0], pos[1]+i+1))
				length2[(pos[0], pos[1]+i+1)] = steps2
			pos[1] = pos[1] + int(direction[1:])
		if direction[0] == "D":
			for i in range(int(direction[1:])):
				steps2 +=1
				#print(direction[1:])
				input2.add((pos[0], pos[1]-i-1))
				length2[(pos[0], pos[1]-i-1)] = steps2
			pos[1] = pos[1] - int(direction[1:])
		if direction[0] == "R":
			for i in range(int(direction[1:])):
				steps2 +=1
				#print(direction[1:])
				input2.add((pos[0]+i+1, pos[1]))
				length2[(pos[0]+i+1, pos[1])] = steps2
			pos[0] = pos[0] + int(direction[1:])
		if direction[0] == "L":
			for i in range(int(direction[1:])):
				steps2 +=1
				#print(direction[1:])
				input2.add((pos[0]-i-1, pos[1]))
				length2[(pos[0]-i-1, pos[1])] = steps2
			pos[0] = pos[0] - int(direction[1:])

	intersections = input1.intersection(input2)
	distances = set()
	wiredistances = set()
	for item in intersections:
		distances.add(((abs(item[0]) + abs(item[1])), length1[item], length2[item]))
	for item in distances:
		wiredistances.add(item[1] + item[2])
	return (pos, input1, input2, intersections, distances, wiredistances)


print(min(intersections(inputlist1,inputlist2)[5]))






