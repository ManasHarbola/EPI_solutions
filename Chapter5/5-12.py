def random_sampling(k, A):
    for i in range(k):
        randIdx = random.randint(i, len(A) - 1)
        A[i], A[randIdx] = A[randIdx], A[i]
