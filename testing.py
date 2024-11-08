def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def printnprimes(n):
    c = 0
    i = 2
    while c < n:
        if isprime(i):
            print(i, end=" ")
            c += 1
        i += 1


n = int(input())
print("First", n, "primes: ", end="")
printnprimes(n)
print("\n")
