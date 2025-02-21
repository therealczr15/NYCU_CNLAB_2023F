num = int(input())
validList  = []
for i in range(num):
    sum = 0
    cardCode = list(map(int, input().split()))
    for j in range(4):
        count = 0
        while count < 4:
            if count % 2 == 0:
                sum += cardCode[j] % 10
            else:
                if (cardCode[j] % 10) * 2 >= 10:
                    sum += (((cardCode[j] % 10) * 2) % 10) + (((cardCode[j] % 10) * 2) // 10)
                else:
                    sum += ((cardCode[j] % 10) * 2)
            count += 1
            cardCode[j] //= 10
    #print("sum = ",sum)
    if sum % 10 == 0: 
        validList.append(True)
    else: 
        validList.append(False)
for i in validList:
    if i:
        print("Valid")
    else:
        print("Invalid")   