


a = [0] * 10

for i in range(10) :
  a[i] = int(input()) % 42


result = list(set(a))

print(len(result))

