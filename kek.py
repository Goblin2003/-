a = []
n = int(input(''))
for i in range(0,n):
	b = int(input(''))
	a.append(b)
for b in a:
	if int(b) % 2 == 0:
		print("ответ", b)
