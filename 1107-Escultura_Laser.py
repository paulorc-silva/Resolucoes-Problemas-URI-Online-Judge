while(True):
	a, c = list(map(int, input().split()))

	if((a == 0) and (c == 0)):
		break

	x = list(map(int, input().split()))

	count = a - x[0]

	for i in range(0, len(x), 1):
		if(i != (len(x) - 1)):
			if(x[i] > x[i + 1]):
				count += x[i] - x[i + 1]

	print(count)
