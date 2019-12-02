

with open("input2.txt") as file1:
	program = file1.read().split()[0].split(",")
	for i in range(len(program)):
		program[i] = int(program[i])

def read1(index,list1):
	if list1[index] == 1:
		list1[list1[index + 3]] = list1[list1[index + 1]] + list1[list1[index + 2]]
		read1(index + 4, list1)
	elif list1[index] == 2:
		list1[list1[index + 3]] = list1[list1[index + 1]]*list1[list1[index + 2]]
		read1(index + 4, list1)
	elif list1[index] == 99:
		sdfj = 2

for i in range(99):
	for j in range(99):
		program1 = program.copy()
		program1[1] = i
		program1[2] = j
		read1(0,program1)
		if(program1[0] == 19690720):
			print((i,j))
			break
