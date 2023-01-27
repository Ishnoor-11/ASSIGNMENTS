x = int(input("Enter marks of the student "))

if(x>80):
    print("Your Grade Is : A")
elif(x<=80 & x>60):
    print("Your Grade Is : B")
elif(x<=60 & x>50):
    print("Your Grade Is : C")
elif(x<=50 & x>45):
    print("Your Grade Is : D")
elif(x<=45 & x>25):
    print("Your Grade Is : E")
elif(x<25):
    print("Your Grade Is : F")
else:
    print("ERROR")

