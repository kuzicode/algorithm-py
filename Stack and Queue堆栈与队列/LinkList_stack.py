'''
链表（Linked List）
堆栈的链表实现插到元素前面，因此都是对第一个节点进行操作
下面模块导入自我的链表学习笔记代码
'''
from LinkedList import LinkedList
from LinkedList import Node

class LinkedStack(object):
    def __init__ (self):
        self._list = LinkedList()
        
    def __len__ (self):
        return self._list.length
    
    def is_empty(self):
        return self._list.length == 0
    
    # O(1)
    def push(self, e):
        self._list.add_first(e);
        
    # O(1)
    def top(self):
        return self._list.get_first().value;
    
    # O(1)
    def pop(self):
        return self._list.remove_first().value;
        
    def printstack(self):
        self._list.printlist()
        
mystack = LinkedStack()
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

#输出结果
size was:  0
size was:  5
5 4 3 2 1 
size was:  3
3 2 1 
3