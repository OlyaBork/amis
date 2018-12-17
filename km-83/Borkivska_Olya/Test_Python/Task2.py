first = int(input("Введіть перший елемент "))
second = int(input("Введіть останній елемент "))
newlist = tuple(range(first,second+1))
print(newlist)
count = 0
for i in newlist:
    if i%2==0:
        None
    else:
        count+=1

print("Кількість непарних чисел: ",count)