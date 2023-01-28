S1=input()
S2=input()
n=len(S1)
m=len(S2)
dp=[]
for i in range(n+1):
  dp.append([0 for j in range(m+1)])
result=0
for i in range(n+1):
  if(i==0):
      continue
  for j in range(m+1):
      if(j==0):
          continue
      if(S1[i-1]==S2[j-1]):
          dp[i][j]=dp[i-1][j-1]+1
          result=max(result,dp[i][j])
      else:
          dp[i][j]=0
print(result)
