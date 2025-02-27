import sys

inputText = input()

inputTextSlice = []
inputTextSliceCount = [0,0]

tempString = inputText[0]
for i in range(1,len(inputText)):
  if inputText[i] == tempString[-1]:
    tempString += inputText[i]
  else:
    inputTextSlice.append(tempString)
    tempString = inputText[i]


inputTextSlice.append(tempString)


for i in inputTextSlice:
  if i[0] == '0':
    inputTextSliceCount[0]  += 1
  else:
    inputTextSliceCount[1] += 1

print(min(inputTextSliceCount))
  
    
  