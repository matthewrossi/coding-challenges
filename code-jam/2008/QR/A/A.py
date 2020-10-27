n = int(input())
for i in range(1, n + 1):
	s = int(input())
	engines = {}
	for j in range(s):
		engines[str(input())] = True
	q = int(input())
	
	switches = 0
	available_engines = s
	for j in range(q):
		query = str(input())
		if engines[query] == True:
			if available_engines > 1:
				engines[query] = False
				available_engines -= 1
			else:
				switches += 1
				available_engines = s - 1
				for key in list(engines.keys()):
					engines[key] = True
				engines[query] = False

	print ("Case #{}: {}".format(i, switches))
