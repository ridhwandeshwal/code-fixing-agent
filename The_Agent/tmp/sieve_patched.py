def sieve(max):
    primes = []
    for n in range(2, max + 1):
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes