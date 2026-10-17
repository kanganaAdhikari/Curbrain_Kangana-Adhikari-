import ast

MOD = 10**9 + 7

arr = ast.literal_eval(input())

result = 0

for value in arr:
    result = (result + value) % MOD

print(result)
