string= str(input("Enter a string"))
a=""
for i in range(len(string)):
    a=string[i]+a
print(a)