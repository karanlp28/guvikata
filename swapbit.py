n,k=map(int,input().split())
for i in range(1):
    temp=n|k
    n,k=temp&k,temp&n
print(n,k)
