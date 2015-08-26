def xgcd(a,b):
	prevx, x = 1, 0
	prevy, y = 0, 1
	while b:
		q = a/b
		x, prevx = prevx - q*x, x
		y, prevy = prevy - q*y, y
		a, b = b, a % b				
	return prevx

def monpro(a,b,r,n):
	result = False
	x = xgcd(r,n)
	n1 = (1+(r*x))/n
	t = a*b
	m = (t*n1)%r
	u = (t+(m*n))/r
	if u>n:
		u = u-n
		result = True
		return u, result 
	else:
		return u, result
	

def monexp(g,a,r,p):
	global truth_bucket
	global false_bucket
	l = len(bin(a))
	b = bin(a)
	c = 3
	m1 = (g*r)%p
	c1 = r%p
	e1,result = monpro(c1,c1,r,p)
	e2, result = monpro(e1,m1,r,p)
	iter = 1
	for c in range (c,l):
		if '0' in b[c]:
			e1, result = monpro(e2,e2,r,p)
		else:
			e1, result = monpro(e1,e1,r,p)
			e1, result = monpro(e1,m1,r,p)
			if result == True:
				truth_bucket[iter] += 1	
				truth_time_bucket[iter] += 5
			else:
				false_bucket[iter] += 1
				false_time_bucket[iter] += 0.5
		iter += 1	
				
	return e1	

d_bits = 9
truth_bucket = [0 for x in range(15)]
false_bucket = [0 for y in range(15)] 	

truth_time_bucket = [0 for x in range(15)]
false_time_bucket = [0 for y in range(15)] 	
		
	
print('Enter in the following order g, a, r, p')
import random
a = 127
r = 1024
p = 553
for num in range(100):
	g = random.randint(1000,10000)
	m1 = (g*r)%p
	exp1 = monexp(g,a,r,p)
	ans = monpro(exp1,m1,r,p)
	print (g, ans)

print truth_bucket
print truth_time_bucket
print false_bucket
print false_time_bucket
	


