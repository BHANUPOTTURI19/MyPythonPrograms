l=[0,1,0,1,1,1,0,0,0,0]
i=0
c=0
for i in range(0,len(l)):
    while(l[i]==1):
        c+=1
        break;
print(c)

