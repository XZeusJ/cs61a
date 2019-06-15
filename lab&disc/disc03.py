# 1.1 iterative version
def is_prime_iter(n):
	if n == 1 or n == 2: return False
	division = 2
	while (division < n-1):
		if n % division == 0:
			return False
		division +=1
	return True

# print(is_prime_iter(7))
# print(is_prime_iter(10))
# print(is_prime_iter(1))

# 1.1 recursion version
def is_prime(n):
	if n == 1 or n == 2: return False
	def prime_helper(division):
		if division == 2: return True
		if n % division == 0:
			return False
		else:
			return prime_helper(division-1)
	return prime_helper(n-1)

# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(1))

# 1.2
def make_func_repeater(f, x):
	def repeater(n):
		if n == 1: 
			return f(x)
		else:
			return f(repeater(n-1))
	return repeater
incr_1 = make_func_repeater(lambda x: x + 1, 1)
# print(incr_1(2))
# print(incr_1(5))

# 2.1
def count_stair_ways(n):
	if n <= 2:
		return n
	return count_stair_ways(n-1)+count_stair_ways(n-2)
# print(count_stair_ways(1))
# print(count_stair_ways(2))
# print(count_stair_ways(3))
# print(count_stair_ways(4))

# 2.2
result = 0
def count_k(n, k):
	if n <= k:
		return n
	for i in range(1, k+1):
		result += count_k(n-i)
	return result
print(count_k(4,4))