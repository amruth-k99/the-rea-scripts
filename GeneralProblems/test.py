dists = int(input())
inp = input().split(' ')
numbers = input().split(' ')
digits = ord(inp[1])-ord(inp[0])
if digits < 0:
    digits = digits*-1

print(dists*pow(len(numbers), 4)*pow(digits+1, 2))
