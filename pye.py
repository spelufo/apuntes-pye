############################################## CONTEO

def factorial(n, down_to=0, ammount=None):
	n = int(n)
	down_to = int(down_to)
	if ammount is not None:
		ammount = int(ammount)
	if n < 2 or ammount == 0 or n == down_to:
		return 1
	return n * factorial(n - 1, down_to=down_to, ammount=(ammount-1 if type(ammount) == int else None))

def arreglos(n, k):
	return factorial(n, ammount=k)
A = arreglos

def combinaciones(n, k):
	if k > n or k < 0:
		return 0
	return factorial(n, ammount=k) / factorial(k)
binomial = C = combinaciones

def permutaciones(n, reps=[]):
	res = factorial(n)
	for i in reps:
		res /= factorial(i)
	return res
P = permutaciones


############################################## DISTRIBUCIONES DISCRETAS

def Bin(n,p):
	return lambda k: C(n,k) * p**k * (1-p)**(n-k)

def Ber(p):
	return Bin(1,p)

def Hiper(N, D, n):
	return lambda k: 1.*C(N-D,n-k)*C(D,k)/C(N,n)

def Pois(l):
	return lambda k: np.exp(-l)*l**k/factorial(k)

def BinNeg(r,p):
	return lambda k: C(k-1,r-1) * p**r * (1-p)**(k-r)

def Geo(p):
	return BinNeg(1,p)
