'''
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[i] + a[j] == n:
            check = True
print(check)

dict["3"] = 3
dict[4] = 32
print(dict)
'''
a = [1, 4, 5, 7]
dict = {}
dict[1] = 5
dict[2] = 6
dict[3] = 8
dict[4] = 9
dict[5] = 11
dict[6] = 12
check = False
for i in range(len(a)):
    n = 5
    x = n - a[i]
    if x == a[i]:
        continue

    try:
        dict[x]
        check = True
        break
    except:
        continue
print(check)