numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list1 = numbers[::-1]
print(list1)
print(numbers)
___________________________

prices = [135, -345, 785, 0, -100, 500]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)

oddEven = ["홀수" if i % 2 == 1 else "짝수" for i in range(10)]
print(oddEven)
____________________________
s = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

for i in range(len(s)):
    for j in range(len(s[i])):
        s[i][j] = s[i][j] * 2
print(s)


set = {1, 2, 3}
print(set1)

for i in set1:
    print(i)