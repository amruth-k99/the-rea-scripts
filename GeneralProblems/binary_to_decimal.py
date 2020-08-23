import sys


def bin_convert(n):
    dec = 0
    p = 0
    rem = 0
    while n > 0:
        rem = n % 10
        if rem is 1:
            dec = dec + 2**p
        if rem is not 1 and rem is not 0:
            return ("Please enter correct Binary value")

        p = p+1
        n = int(n/10)
    return dec


def main():
    n = sys.argv[1]
    decimal = bin_convert(int(n))
    print("Decimal Equivalent: "+str(decimal))


if __name__ == "__main__":
    main()
    pass
