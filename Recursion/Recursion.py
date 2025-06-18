

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    num = 6
    print(factorial(n=num))

    print(fibo(n=num))

