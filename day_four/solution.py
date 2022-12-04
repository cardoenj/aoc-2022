
pairs = []
with open("input.dat") as fp:
    pairs = fp.readlines()

def is_in(a, b):
    a = [int(a[0]), int(a[1])]
    b = [int(b[0]), int(b[1])]
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    if b[0] >= a[0] and b[1] <= a[1]:
        return True
    return False

def is_partially_in(a, b):
    a = [int(a[0]), int(a[1])]
    b = [int(b[0]), int(b[1])]

    if a[0] < b[0] and a[1] < b[0]:
        return False
    if a[0] > b[1] and a[1] > b[1]:
        return False
    
    return True

print(is_partially_in([5, 7], [8,9]))
total = 0
total_partial = 0
for pair in pairs:
    splitted = pair.replace("\n", "").split(",")
    first = splitted[0].split("-")
    second = splitted[1].split("-")
    total += int(is_in(first, second))
    total_partial += int(is_partially_in(first, second))
print(total)
print(total_partial)
