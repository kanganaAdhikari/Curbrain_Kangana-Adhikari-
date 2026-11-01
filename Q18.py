
def reverse_subsegment(arr, start, end):

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1

    return arr


arr = list(map(int, input("Enter array elements: ").split()))
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

reverse_subsegment(arr, start, end)

print(arr)
