# define fn about reverse digit by recursion
def reverse_rec(n,rmd = 0):
	if n == 0:
		print(rmd);
	else:
		# print(n//10);	# current number except last digit
		# print(10*rmd+(n%10)); # reverse number except curent digit
		reverse_rec(n // 10, 10 * rmd + (n%10));
# reverse_rec(123);

# define fn about reverse digit by iteration
def reverse_iter(n):
	i = 0;
	reverse = 0;
	while (n != 0):
		# print("n:",n)
		reminder = n%10
		reverse = (reverse*10)+reminder
		# print("reverse:",reverse)
		n //= 10;
	return reverse
# print(reverse_iter(123))

def isMutiple(s, k):
	return (s%k == 0) and s!=0 and s!=k; 

def print_numbers(n, k):
	def inner(n, s):
		if n==0:
			# print(s);
			if isMutiple(s, k):
				print(s);
		else:
			inner(n // 10, 10*s+(n%10));
			inner(n // 10, s);
	inner(n, 0);
	print();

# print_numbers(97531, 5);
# print_numbers(97531, 7);
# print_numbers(97531, 2);

def sixty_ones(n):
	if n == 0:
		return 0;
	elif n % 100 == 61:
		return sixty_ones(n // 10) + 1;
	else:
		return sixty_ones(n // 10);
# print(sixty_ones(461601))
# print(sixty_ones(161461601))

def no_elevens(n):
	if n == 0:
		return 1;
	# elif :
		# return no_elevens(n-1) - n;
	else:
		return no_elevens(n-1)*2-(n-1);
print(no_elevens(2));
print(no_elevens(3));

