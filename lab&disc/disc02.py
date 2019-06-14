def is_even(x):
	return x%2==0

def keep_ints(cond, n):
	for i in range(1,n+1):
		if cond(i):
			print(i)

# keep_ints(is_even,5)

def keep_ints2(n):
	def fn(f):
		for i in range(1, n+1):
			if f(i):
				print(i)
	return fn
# keep_ints2(5)(is_even)


# 2.1
def multiply(m, n):
	if n == 1: return m
	return m + multiply(m, n-1)
# print(multiply(5,3))

# 2.2
def countdown(n):
	print(n)
	if n == 1:
		pass
	else:
		return countdown(n-1)
# countdown(3)

# 2.3
def countup(n):
	def help(k):
		print(n-k)
		if n-k == n:
			pass
		else:
			return help(k-1)
	help(n)
# countup(3)

# 2.4
def sum_every_other_digit(n):
	if n == 0:
		return 0
	else:
		return n % 10 + sum_every_other_digit(n // 100)

print(sum_every_other_digit(228))
print(sum_every_other_digit(1234567))