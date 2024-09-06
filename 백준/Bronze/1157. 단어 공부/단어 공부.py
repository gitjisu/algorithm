import sys


word = input().strip()


# M I S P
alphabet = []
alphabetCnt = []


for w in word :
  if w.upper() in alphabet :
    pass
  else :
    alphabet.append(w.upper())
    alphabetCnt.append(0)




for i in range(len(word)) :
  alphabetCntIndex = alphabet.index(word[i].upper())
  alphabetCnt[alphabetCntIndex] += 1




max_count = max(alphabetCnt)


max_count_appear = alphabetCnt.count(max_count)

if max_count_appear > 1 :
  print('?')
else :
  resultIndex = alphabetCnt.index(max_count)
  print(alphabet[resultIndex])

