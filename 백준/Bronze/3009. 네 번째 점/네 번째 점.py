

x_arr = []
y_arr = []
x_temp = []
y_temp = []
x_duplicate = 0
y_duplicate = 0

for _ in range(3) :
  x, y = map(int, input().split())
  x_arr.append(x)
  y_arr.append(y)


for x in range(len(x_arr)):
  if x_arr[x] not in x_temp:
    x_temp.append(x_arr[x])
  else :
    x_duplicate = x_arr[x]


for y in range(len(y_arr)) :
  if y_arr[y] not in y_temp :
    y_temp.append(y_arr[y])
  else :
    y_duplicate = y_arr[y]


while x_duplicate in x_arr :
  x_arr.remove(x_duplicate)

while y_duplicate in y_arr :
  y_arr.remove(y_duplicate)

print(('').join(map(str, x_arr)), ('').join(map(str, y_arr)))