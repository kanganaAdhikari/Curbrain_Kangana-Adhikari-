
def threshold_filter(arr, threshold):
    result = []

    for i in range(len(arr)):
        if arr[i] >= threshold:
            result.append(arr[i])

    return result


arr = list(map(int, input("Enter array elements: ").split()))
threshold = int(input("Enter threshold: "))

print(threshold_filter(arr, threshold))
