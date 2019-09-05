def permutations(seq):

    if not seq:
        yield []
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + [seq[0]] + perm[i:]


print(sorted(permutations([1,2,3])))
