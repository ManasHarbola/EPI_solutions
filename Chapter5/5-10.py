def apply_permutation(perm, A):
    for i in range(len(A)):
        nextIdx = i
        while perm[nextIdx] >= 0:
            A[i], A[perm[nextIdx]] = A[perm[nextIdx]], A[i]
            temp = perm[nextIdx]
            perm[nextIdx] -= len(A)
            nextIdx = temp

