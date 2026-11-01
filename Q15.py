
def minimum_absolute(arr):
    minimum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            current = -arr[i]
        else:
            current = arr[i]

        if minimum < 0:
            minimum_abs = -minimum
        else:
            minimum_abs = minimum

        if current < minimum_abs:
            minimum = arr[i]

    return minimum


arr = list(map(int, input("Enter array elements: ").split()))

print(minimum_absolute(arr))
