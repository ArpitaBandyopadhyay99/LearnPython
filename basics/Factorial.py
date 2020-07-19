userInput = 5
result = 1

# for i in range(userInput+1):
#    if i == 0:
#        result = 1
#    else:
#        result = result * i


j = userInput
while j > 0:
    if j == 0:
        result = 1
        break
    else:
        result = result * j
        j -= 1

print("input: ", userInput, "result: ", result)
