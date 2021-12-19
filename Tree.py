#%%
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


#%%
def recursivePreorder(node): 
  if node is None:
    return 
  print(node.val, end=' ')
  recursivePreorder(node.left) 
  recursivePreorder(node.right)

def iterativePreorder(node):
  if node is None:
    return
  stack = []
  stack.append(node)
  while 0<len(stack):
    pop_node = stack.pop()
    print(pop_node.val, end=' ')
    if pop_node.right:
      stack.append(pop_node.right)
    if pop_node.left:
      stack.append(pop_node.left)

# 1 2 4 5 3 6 7  
#%%
def recursiveInorder(node): 
  if node is None:
    return 
  recursiveInorder(node.left) 
  print(node.val, end=' ')
  recursiveInorder(node.right)

def iterativeInorder(node):
  crnt_node = node
  stack = []
  while True:
    if crnt_node is not None:
      stack.append(crnt_node)
      crnt_node = crnt_node.left
    
    elif 0<len(stack):
      crnt_node = stack.pop()
      print(crnt_node.val, end=' ')
      crnt_node = crnt_node.right
    else:
      break
# 4 2 5 1 6 3 7  
 
#%%
def recursivePostorder(node): 
  if node is None:
    return 
  recursivePostorder(node.left) 
  recursivePostorder(node.right)
  print(node.val, end=' ')

def iterativePostorder(node):
  stack = []
  last_visit_node = None
  crnt_node = node
  while True:
    if crnt_node is not None:
      stack.append(crnt_node)
      crnt_node = crnt_node.left
    
    elif 0<len(stack):
      peek_node = stack[-1]
      if peek_node.right and last_visit_node != peek_node.right:
        crnt_node = peek_node.right
      else:
        print(peek_node.val, end=' ')
        last_visit_node = stack.pop()
        
    else:
      break

# 4 5 2 6 7 3 1

#%%
from collections import deque

def treeLevelPrint(node):
  if node is None:
    return
  q = deque()
  q.append(node)
  while 0<len(q):
    crnt_node = q.popleft()
    print(crnt_node.val, end = ' ')
    if crnt_node.left:
      q.append(crnt_node.left)
    if crnt_node.right:
      q.append(crnt_node.right)
    
#1 2 3 4 5 6 7  



def treeLevelPrint2(node):
  if node is None:
    return
  q = deque()
  q.append(node)
  while 0<len(q):
    level_count = len(q)
    for _ in range(level_count):
      crnt_node = q.popleft()
      print(crnt_node.val, end = ' ')
      if crnt_node.left:
        q.append(crnt_node.left)
      if crnt_node.right:
        q.append(crnt_node.right)
    print('')

# 1 
# 2 3 
# 4 5 6 7 




#%%
# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)

# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7
# recursivePreorder(node1)
# print(' ')
# iterativePreorder(node1)
# print(' ')

# recursiveInorder(node1)
# print(' ')
# iterativeInorder(node1)
# print(' ')
# recursivePostorder(node1)
# print(' ')
# iterativePostorder(node1)
# # %%
# treeLevelPrint(node1)
# print(' ')
# treeLevelPrint2(node1)
# %%
class TreeNode2:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Isfull(node):
    if node.left is not None and node.right is not None:
      return True
    else:
      return False

class CompleteBinaryTree:
    def __init__(self):
        self.root = None
    

    def Insert(self, val):
      from collections import deque
      queue = deque([])
      new_node = TreeNode2(val)
      queue.append(self.root)
      
      while(True):
        if queue[0].left == None:
          queue[0].left = new_node
          break
        elif queue[0].right == None:
          queue[0].right = new_node
          break
        else:
          queue.append(queue[0].left)
          queue.append(queue[0].right)
          queue.popleft()
    
    def recursivePostorder(self, node): 
      if node is None:
        return
      self.recursivePostorder(node.left) 
      self.recursivePostorder(node.right)
      print(node.val, end=' ')

#%%



cbt = CompleteBinaryTree()
node1 = TreeNode2(1)
cbt.root=node1


#%%
for i in range (2,7,1):
  cbt.Insert(i)

# %%
cbt.recursivePostorder(cbt.root)





# %%
