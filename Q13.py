import ast

arr = ast.literal_eval(input())
k = int(input())

prefix_sum = 0
found = False

for value in arr:
    prefix_sum += value

    if prefix_sum % abs(k) == 0:
        found = True
        break

print(found)
