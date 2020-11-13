n = int(input())
count = n
if(n > 20):
    print("WRONG INFRASTRUCTURE")
else:
    # with 2
    s = int(n / 2)
    if(n % 2):
        s += 1
    count += s
    print(count)
