a=set("123456789")
b=[]
for i in range(1,10000):
    c=1
    strnum=""
    while True:
        numara=i*c
        strnum+=str(numara)
        if len(strnum)>=9:
            if len(strnum)>9:
                break
            else:
                if a==set(strnum):
                    b.append(int(strnum))
        c+=1
print(max(b))
