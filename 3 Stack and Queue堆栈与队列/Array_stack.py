
# 动态数组堆栈（Array Stack）
# 堆栈的数组实现插到数组后面，因此基本都是对最后一个元素进行操作

class ArrayStack(object):
    def __init__ (self):
        self._data = [] #空的容器
        
    def __len__ (self): #size
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    # push进堆栈： O(1)
    def push(self, e):
        self._data.append(e)
        
    # 查看栈顶元素：O(1)
    def top(self):           
        if self.is_empty( ):
            raise ValueError( 'Stack is empty' )
        return self._data[-1]
    
    # 弹出栈顶元素 O(1)
    def pop(self):
        if self.is_empty( ):
            raise ValueError( 'Stack is empty' )
        return self._data.pop( )  
    
    # 打印堆栈
    def printstack(self):   
        for i in range(len(self._data)):
            print(self._data[i], end = ' ')
        print()

if __name__ == "__main__":
    mystack = ArrayStack()
    print ('size was: ', str(len(mystack)))
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)
    print ('size was: ', str(len(mystack)))
    mystack.printstack()
    mystack.pop()
    mystack.pop()
    print ('size was: ', str(len(mystack)))
    mystack.printstack()
    print(mystack.top())
    mystack.pop()
    mystack.pop()
    mystack.pop()

