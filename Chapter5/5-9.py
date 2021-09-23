def generate_primes(n):
    isPrimeList = [False] + ([True] * (n - 1))
    primes = []

    for i in range(1, n):
        if isPrimeList[i]:
            primes.append(i + 1)
        for j in range(i, n, i + 1):
            isPrimeList[j] = False


    return primes
