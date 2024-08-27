
word = input()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w','x','y','z']
result = [-1 for i in range(26)]

for w in range(len(word)) :
  
  alphabetIndex = alphabet.index(word[w])
  if (result[alphabetIndex] == -1) :
    result[alphabetIndex] = w

  


print(" ".join(map(str, result)))
  

