
def longestArithmetic(arr):
    longest = 0
    temp = 0
    diff = '1'
    for x in range(0, len(arr)-1):
        if isinstance(diff, str):
            diff = 0
        if diff is arr[x]-arr[x+1]:
            temp += 1
        else:
            temp = 1
        diff = arr[x]-arr[x+1]
        if temp > longest:
            longest = temp

    return longest+1


t = int(input())
ans = []
for x in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    ans.append(longestArithmetic(arr))
for y in ans:
    print("Case #{}: {}".format(x+1, y), flush=True)
 # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Kick Start problems.
