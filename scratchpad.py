from urllib.parse import quote, unquote

list1 = [1, 1, 2, 2, 3, 3, 4, 5, 6 ,7 ,8]
for i in range(len(list1)):
    print(max(list1))
    list1.remove(max(list1))
print(len(list1))