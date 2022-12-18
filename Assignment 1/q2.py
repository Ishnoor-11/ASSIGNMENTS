x = int(input("Enter Your Gross Income"))
y = int(input("Enter number of dependent people="))
z = 10000                                             # z = standard deduction
w = 3000                                              # w = additional deduction
v = x-z-(w*y)                                         # v = taxable income
tax = v*0.2                                           # flat tax rate = 20%
print("Tax = ",tax)