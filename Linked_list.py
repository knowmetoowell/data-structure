#%%
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# head_node = Node(1)
# head_node.next = Node(2)


def printNodes(node:Node):
    curr_node = node
    while curr_node is not None:
        print(curr_node.val, "-> ",end=' ')
        curr_node = curr_node.next


class single_linked_list:
    def __init__(self):
        self.head = None       

    def addAtHead(self, val): # O(1)
        node = Node(val)
        node.next = self.head
        self.head = node
    
    # 리스트에 아무것도 없을때는 작동안함
    def addAtTail(self, val):# O(N)
        node = Node(val)
        curr_node= self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        
    def findNode(self, val):# O(N)
        curr_node = self.head
        while curr_node is not None:
            if curr_node.val == val:
                return curr_node
            curr_node = curr_node.next
        raise RuntimeError('Node not Fount')
    
    # 뉴노드를 만들고 
    # 삽입하고자 하는 위치의 노드를 받아와서 
    # 그 노드의 넥스트를 뉴노드로 하고 뉴노드의 넥스트를 그 노드의 넥스토 지정
    
    def Insert(self, node, val):# O(1)
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node

    # 지우고자 하는 전 노드를 받아와서 전 노드의 넥스트를 넥스트넥스트로 바꿈
    # 매니지드 랭귀지인 파이썬에서는 자동으로 메로리에서 삭제댐
    def DeleteAfter(self, prev_node):# O(1)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next
    
    # 지우고 싶은 곳 지우기
    def DeleteAt(self, val):
        if val == self.head.val:
            self.head = self.head.next
            return
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            if curr_node.val == val:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next 



    def IsCircular(self): # 서클화 링크드리스트인지 판별하기
        curr_node = self.head
        list_node = []
        while(True):
            if curr_node.next is None:
                return False
            list_node.append(curr_node)
            curr_node = curr_node.next 
            if curr_node in list_node:
                return True

    def Circular(self):#서클화 만들기
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = self.head
    
    def None_Circular(self):#서클화 풀기
        curr_node = self.head
        list_node = []
        while(True):
            list_node.append(curr_node)
            if curr_node.next in list_node:
                curr_node.next = None
                break
            curr_node = curr_node.next
    
    

#%%
class Node2:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
def printNodes(node:Node2):
    curr_node = node
    while curr_node is not None:
        print(curr_node.val, "<-> ",end=' ')
        curr_node = curr_node.next

class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addAtHead(self, val): # O(1)
        node = Node2(val)
        node.next = self.head
        self.head = node
        self.head.next.prev = node
    
    
    def addAtTail(self, val):# O(N)
        node = Node2(val)
        if self.head is None:
            self.head = node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        self.tail = curr_node.next
        curr_node.next.prev = curr_node

    def Insert(self, node, val):# O(1)
        new_node = Node2(val)
        new_node.next = node.next
        node.next.prev = new_node
        new_node.prev = node
        node.next = new_node
        
    def findNode(self, val):# O(N)
        curr_node = self.head
        while curr_node is not None:
            if curr_node.val == val:
                return curr_node
            curr_node = curr_node.next
        raise RuntimeError('Node not Fount')
    
    def Delete(self, val):
        curr_node = self.findNode(val)
        if curr_node == self.head:
            self.head = curr_node.next
            self.head.prev = None
        else:
            curr_node.next.prev = curr_node.prev
            curr_node.prev.next = curr_node.next
            
        
                

        
#%%
slist = single_linked_list()
# slist.addAtTail(1)
slist.addAtHead(50)
slist.addAtHead(60)
slist.addAtTail(30)
slist.addAtTail(4)
slist.addAtTail(10)

node1 = slist.findNode(30)

slist.Insert(node1, 7)
printNodes(slist.head)
slist.DeleteAt(60)
printNodes(slist.head)
a = slist.IsCircular()
slist.Circular()
print(a)
a = slist.IsCircular()
print(a)
slist.None_Circular()
a = slist.IsCircular()
print(a)

# %%
dlist = Double_linked_list()
dlist.addAtTail(30)
dlist.addAtTail(10)
dlist.addAtTail(35)
dlist.addAtTail(15)
dlist.addAtTail(40)

printNodes(dlist.head)
# %%
