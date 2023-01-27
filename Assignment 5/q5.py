x = int (input("Enter number of rows "))
k = ord("A")
for i in range (x):
    for j in range (i+1):
        print (chr(k) , end="")
        k=k+1
        if(k>90):
            k=65
            continue
    print()