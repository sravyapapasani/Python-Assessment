def sumUptoTarget(nums,target):
    for i in nums:
        if target-i in nums and ((2*i!=target) or (nums.count(i)>1)):
            return (i,target-i)

l=list(map(int,input().split()))
target=int(input())
print(sumUptoTarget(l,target))
