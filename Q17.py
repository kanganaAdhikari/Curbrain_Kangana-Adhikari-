
def most_popular(sales):
    frequency = {}

    for i in range(len(sales)):
        if sales[i] in frequency:
            frequency[sales[i]] += 1
        else:
            frequency[sales[i]] = 1

    highest = 0
    result = None

    for item in frequency:
        if frequency[item] > highest:
            highest = frequency[item]
            result = item

        elif frequency[item] == highest:
            if item < result:
                result = item

    return result


sales = list(map(int, input("Enter product IDs: ").split()))

print(most_popular(sales))
