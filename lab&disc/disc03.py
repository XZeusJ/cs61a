# 1.1 iterative version
def is_prime_iter(n):
    if n == 1 or n == 2: return False
    division = 2
    while (division < n - 1):
        if n % division == 0:
            return False
        division += 1
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
            return prime_helper(division - 1)

    return prime_helper(n - 1)


# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(1))

# 1.2
def make_func_repeater(f, x):
    def repeater(n):
        if n == 1:
            return f(x)
        else:
            return f(repeater(n - 1))

    return repeater


incr_1 = make_func_repeater(lambda x: x + 1, 1)


# print(incr_1(2))
# print(incr_1(5))

# 2.1
def count_stair_ways(n):
    if n <= 3:
        return 2 ** (n - 1)
    return count_stair_ways(n - 1) + count_stair_ways(n - 2) + count_stair_ways(n - 3)


# print(count_stair_ways(1))
# print(count_stair_ways(2))
# print(count_stair_ways(3))
# print(count_stair_ways(10))

# 2.2
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for i in range(1, k + 1):
            total += count_k(n - i, k)
        return total


# def count_k(n, k):
# 	if n <= k:
# 		return 2**(n-1)
# 	else:
# 		total = 0
# 		for i in range(1, k+1):
# 			total += count_k(n-i,k)
# 		return total

print(count_k(3, 3))
print(count_k(4, 4))
print(count_k(5, 3))
print(count_k(300, 1))


# 2.3
def pascal(row, column):
    if row < column: return 0
    if column == 0: return 1
    if row <= 1: return 1
    return pascal(row - 1, column - 1) + pascal(row - 1, column)

# print(pascal(0,0))
# print(pascal(1,0))
# print(pascal(1,1))
# print(pascal(2,0))
# print(pascal(2,1))
# print(pascal(2,2))
# print(pascal(4,2))
