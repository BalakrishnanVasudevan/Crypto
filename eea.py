a = 241	
b = 323

prevx, x = 1, 0; prevy, y = 0, 1
while b:
	q = a/b
	x, prevx = prevx - q*x, x
	y, prevy = prevy - q*y, y
	a, b = b, a % b
	
	
print a