
def second_highest(scores):
    highest = None
    second = None

    for i in range(len(scores)):
        value = scores[i]

        if highest is None or value > highest:
            second = highest
            highest = value

        elif value != highest:
            if second is None or value > second:
                second = value

    if second is None:
        return -1

    return second


scores = list(map(int, input("Enter scores: ").split()))

print(second_highest(scores))
