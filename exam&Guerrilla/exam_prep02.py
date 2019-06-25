# def print_numbers(n, k):
# 	def inner(n, s):
# 		if n == 0:
# 			if n // k == 0:
# 				print(n);
# 		else:

# 	inner(n, 0)

# define fn about reverse digit by recursion
def reverse_rec(n,rmd = 0):
	if n == 0:
		return rmd;
	else:
		return reverse(n // 10, 10 * rmd + (n%10));
# print(reverse_rec(123))

# define fn about reverse digit by iteration
def reverse_iter(n):
	i = 0;
	reverse = 0;
	n = 123
	while (n != 0):
		print("n:",n)
		reminder = n%10
		reverse = (reverse*10)+reminder
		print("reverse:",reverse)
		n //= 10;
# print(reverse_iter)

def generate_any_digits(n):
	pass