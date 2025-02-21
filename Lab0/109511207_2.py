num = int(input())
outList = []
for i in range(num):
    array = list(map(int, input().split()))
    minList = [0,0]
    for j in range(1,array[0]+1):
        if j == array[0]:
            avgDiff = sum(array[1:array[0]+1])//array[0]
        else:
            avgDiff = abs(sum(array[1:j+1])//j - sum(array[j+1:array[0]+1])//(array[0]-j))
        #print("avgDiff " + str(j-1) + " : " + str(avgDiff))
        if j == 1:
            minList = [avgDiff,0]
        else:
            if avgDiff < minList[0]:
                minList = [avgDiff,j-1]
    outList.append(minList[1])
for i in outList:
    print(i)