base, power, MOD = map(int, input().split())

result = 1 % MOD

for i in range(power):
    result = (result * base) % MOD

print(result)
