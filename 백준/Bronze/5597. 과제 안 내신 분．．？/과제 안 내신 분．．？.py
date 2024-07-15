

student = [i for i in range(1, 31)]

for i in range(1, 29) :
  delete = int(input())
  if delete in student:
    student.remove(delete)

print("\n".join(map(str, student)))
    