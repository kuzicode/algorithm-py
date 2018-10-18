
# 二分查找树
# 构造节点
class Node(object):
    __slots__ = '_item' , '_lchild' , '_rchild'

    def __init__ (self, item, lchild=None, rchild=None):
        self._item = item
        self._lchild = lchild
        self._rchild = rchild

'''
BST操作方法:
BST 搜索
BST 插入
BST获取最小值与最大值
BST 删除
'''

# 搜索
# Get树元素的方法
    def get(self, key):
        return self.__get(self._root, key)

    def __get(self, node, key): # helper
        if (node is None):
            return None
        if (key == node._item):
            return node._item
        if (key < node._item):
            return self.__get(node._lchild, key)
        else:
            return self.__get(node._rchild, key)

# 插入
# add元素的方法
    def add(self, value):
        self._root = self.__add(self._root, value)
        
    def __add(self, node, value): # return node ,helper
        if (node is None):
            return Node(value)
        if (value == node._item):
            pass
        else:
            if (value < node._item):
                node._lchild = self.__add(node._lchild, value)
            else:
                node._rchild = self.__add(node._rchild, value)
        return node 

# 删除
# remove树元素的方法
    def remove(self, key):
        self._root = self.__remove(self._root, key)
        
    def __remove(self, node, key):  # helper
        if node is None:
            return None
        if (key < node._item):
            node._lchild = self.__remove(node._lchild, key)
        elif (key > node._item):
            node._rchild = self.__remove(node._rchild, key)
        else:
            if (node._lchild is None):
                node = node._rchild  
            # if rchild is None,  node = None; case 1: no child  
            # if rchild is not None, node = node._rchild; case 2: one child
            elif (node._rchild is None):
                node = node._lchild
            else:
                node._item = self.__get_max(node._lchild)
                node._lchild = self.__remove(node._lchild, node._item)
                
        return node     

# 获取最大最小值（以下为获取最大值例子）
# get max 元素的方法
    def get_max(self):
        return self.__get_max(self._root)
    
    def __get_max(self, node): # helper
        if (node is None):
            return None
        while (node._rchild is not None):
            node = node._rchild
        return node._item