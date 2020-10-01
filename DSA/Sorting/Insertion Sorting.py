

def insertion_sort(arr):
    # Same as organising the cards
    # Putting a key value a side and inserting it at a particular place
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

    for y in range(1, len(arr)):
        key = arr[y]
        x = y-1
        while x > 0 and key < arr[x]:
            arr[x+1] = arr[x]
            x -= 1
        arr[x+1] = key
    return arr


def merge_sort(arr):
    # Same as organising the cards
    # Putting a key value a side and inserting it at a particular place
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)

    return arr


n = list(map(int, input('Enter the array values: ').split()))
sorted_arr = insertion_sort(n)
print(sorted_arr)
