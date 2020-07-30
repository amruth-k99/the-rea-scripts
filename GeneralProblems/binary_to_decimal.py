def bin_convert(n):
    dec = 0
    p = 0
    rem = 0
    while n > 0:
        rem = n % 10
        if rem is 1:
            dec = dec + 2**p
        p = p+1
        n = int(n/10)
    return dec


def main():
    n = input("Enter the binary: ")
    decimal = bin_convert(int(n))
    print("Decimal Equivalent: "+str(decimal))


if __name__ == "__main__":
    main()
    pass
