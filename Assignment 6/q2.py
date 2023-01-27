string = str(input("Enter a string "))
a=""
s1 = string.replace(" " , "")
for i in range(len(s1)):
    a=s1[i]+a

if (s1== a):
    print(string ,"is a palindrome")
else :
    print(string ,"is not a palindrome")
