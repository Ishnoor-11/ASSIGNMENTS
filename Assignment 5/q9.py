string = str (input("Enter some words : "))
str1 = ' '.join (string.split())
list1 = str1.split()
for i in set(list1):
    print(i, 'occurs :',list1.count(i), 'times')