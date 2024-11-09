def fiborec(n):
    if n <= 1:
        return n
    else:
        return fiborec(n - 1) + fiborec(n - 2)


def fibmemo(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibmemo(n - 1, dp) + fibmemo(n - 2, dp)
    return dp[n]


def fibotab(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fiboptim(n):
    if n <= 1:
        return n
    else:
        a = 0; b = 1; t = 0
        for i in range(2, n + 1):
            t = a + b
            a = b
            b = t
        return t

n = int(input("Enter a number: "))
dp = [-1] * (n + 1)
print(f"The {n}th fibonacci numbers is: {fiboptim(n)}")
