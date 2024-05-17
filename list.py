num=[1,3,8,2,10]  
mx = max(num[0],num[1])
smx = min(num[0],num[1])
for i in range(2,len(num)):
    if num[i] > mx:
        smx=mx
        mx=num[i]
    elif (num[i]>smx and mx!=num[i]):
        smx = num[i]
    
print(smx)
print(mx)

#list methods
print(num)
num.append(4)
print(num)
num.insert(3,5)
print(num)
num.remove(8)
print(num)
num.sort()
print(num)
print(num.clear())
print(num)
