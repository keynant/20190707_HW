#11
str1 = "I love to eat ice cream in the beach"

lst1 = [x.upper() for x in str1]
print(lst1)

lst2 = [x[0] for x in str1.split()]
print(lst2)

lst3 = [x[2] for x in str1.split() if len(x)>2]
print(lst3)

lst4 = [len(x) for x in str1.split()]
print(lst4)

#12

lst1 = [10**i for i in range(10)]
print(lst1)

