lis = []
re_lis = []
def reverse(s):
    for i in s:
        lis.append(i)

    while len(lis) > 0:
        a = lis.pop()
        re_lis.append(a)
    return re_lis

s = 'kumata niubi'
print(reverse(s))