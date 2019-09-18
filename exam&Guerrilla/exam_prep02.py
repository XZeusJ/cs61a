# define fn about reverse digit by recursion
def reverse_rec(n, rmd=0):
    if n == 0:
        print(rmd)
    else:
        # print(n//10);	# current number except last digit
        # print(10*rmd+(n%10)); # reverse number except curent digit
        reverse_rec(n // 10, 10 * rmd + (n % 10))


# reverse_rec(123);

# define fn about reverse digit by iteration
def reverse_iter(n):
    i = 0
    reverse = 0
    while (n > 0):
        # print("n:",n)
        reminder = n % 10
        reverse = (reverse * 10) + reminder
        # print("reverse:",reverse)
        n //= 10
    return reverse


# print(reverse_iter(123))

def is_multiple(s, k):
    return (s % k == 0) and s != 0 and s != k


def print_numbers(n, k):
    def inner(n, s):
        if n == 0:
            # print(s);
            if is_multiple(s, k):
                print(s)
        else:
            inner(n // 10, 10 * s + (n % 10))
            inner(n // 10, s)

    inner(n, 0)
    print()


# print_numbers(97531, 5);
# print_numbers(97531, 7);
# print_numbers(97531, 2);

def sixty_ones(n):
    if n == 0:
        return 0
    elif n % 100 == 61:
        return sixty_ones(n // 10) + 1
    else:
        return sixty_ones(n // 10)


# print(sixty_ones(461601))
# print(sixty_ones(161461601))

def no_elevens(n):
    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    a[0] = b[0] = 1
    for i in range(1, n):
        a[i] = a[i - 1] + b[i - 1]
        b[i] = a[i - 1]
    return a[n - 1] + b[n - 1]


print(no_elevens(2))
print(no_elevens(3))
print(no_elevens(4))
print(no_elevens(5))


def no_elevens_rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return no_elevens_rec(n - 1) + no_elevens_rec(n - 2)


print(no_elevens_rec(2))
print(no_elevens_rec(3))
