num = int(input())
outList = []
for i in range(num):
    n, s = map(int,input().split())
    an = list(map(int, input().split()))
    dp = [float('inf') if i != 0 else 0 for i in range(s+1)]
    for j in range (1,s+1):
        for k in an:
            if j >= k: 
                dp[j] = min(dp[j-k]+1,dp[j])
    outList.append(dp[s])
for i in outList:
    print(i)