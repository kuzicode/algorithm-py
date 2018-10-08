def count(i):
    print(i)
    if i <= 1:
        return i
    else:
        count(i-1)

print(count(5))