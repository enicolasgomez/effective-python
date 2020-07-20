class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None

  def PrintPreOrder(self, indent, last):
    print(indent, end='')

    if last:
      print("└─", end='')
      indent = indent.join("  ")
    else:
      print("├─", end='')
      indent = indent.join("| ")

    print(self.data)

    children = []

    if self.left:
      children.append(self.left)
    if self.right:
      children.append(self.right)

    for i,n in enumerate(children):
      n.PrintPreOrder(indent, i == len(children) -1 )

class BinaryTree:
  def __init__(self, list):
    self.root = Node(list[0])
    for i in list:
      self.addNode(self.root, i)
  
  def Print(self):
    self.root.PrintPreOrder("", True)

  def addNode(self, node, value):
    if value < node.data:
      if node.left == None:
        node.left = Node(value)
      else:
        self.addNode(node.left, value)
    else:
      if node.right == None:
        node.right = Node(value)
      else:
        self.addNode(node.right, value)

treeValues = [ 10, 5, 15, 7, 2, 9, 31 ]
tree = BinaryTree(treeValues)
tree.Print()
