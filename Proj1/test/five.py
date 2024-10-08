val = []
for i in range(10):
    val.append(i)
print(val)


vl = [x for x in range(10)]
print(vl)

even = []
for i in range(10):
    if i%2==0:
        even.append(i)
print(even)

even = [number for number in range(10) if number%2==0]
print(even)