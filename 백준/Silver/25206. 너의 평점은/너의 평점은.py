import sys


score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}
subjects = sys.stdin.read().strip().split('\n')

average = 0.0
cnt = 0.0

for s in subjects :
  l = s.split(' ')
  # 학점
  point = float(l[1])
  # 등급
  grade = l[2]

  if grade != 'P':
    cnt += point
    average += (float(point) * score[grade])
    
# 평균 계산
if cnt == 0:
    result = 0.0
else:
    result = average / cnt

print(f'{result:.6f}')



  

