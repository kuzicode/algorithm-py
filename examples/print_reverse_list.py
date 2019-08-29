def print_reversed(values) :
    # Traverse the list in reverse order, starting with the last element
    # your solution here
    i = len(values) - 1
    reverses = []
    while i > 0: 
        print(values[i],end=',')
        i = i - 1 
    
print_reversed([3,4,52,3,1,5,6,78,3])
 
'''
输出结果
3,78,6,5,1,3,52,4
'''