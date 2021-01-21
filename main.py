import sorting as sort
import selecting as select

def menu():
    print("1. Selection Sort")
    print("2. Selection Sort")

array = []
f = open("array.txt", "r")
for x in f:
    x = int(x)
    array.append(x)

print(sort.bubble_sort(array))

f.close()