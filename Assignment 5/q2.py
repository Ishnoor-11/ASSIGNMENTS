a=int(input ("enter start of range"))
b=int(input ("enter end of range"))
c=int(input ("enter divisible number"))

for i in range(a,b+1):
    if(i%c==0):
        print(i)