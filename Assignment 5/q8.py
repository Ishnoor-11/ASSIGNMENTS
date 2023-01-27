input1 = list(map(int, input('Enter 10 numbers with \' \' separator: ').split()))

positive = []
negative = []
odd = []
even = []

for i in input1:
    if i > 0: positive.append(i)
    if i<0: negative.append(i)
    if i%2 == 0: even.append(i)
    else: odd.append(i)
print('positive: ', positive)
print('negative: ', negative)
print('odd: ', odd)
print('even: ', even)
for i in set(input1):
    print(i, 'occurs :', input1.count(i), 'times')