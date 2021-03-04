data = [1, 3, 5, 7, 9]

with open('test.csv', 'w') as f:
	for p in data:
		p = str(p)
		f.write(str(p[0])+'\n')