

x,y,w,h = map(int, input().split(' '))

# 각 
left = x
right = w-x
top = y
bottom = h-y

print(min(left, right, top, bottom))