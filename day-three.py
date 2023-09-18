import pickle # using pickle pickle to more easily serialize and deserialize our nodes

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# our serialization node
def serialize(root):
    serializeNode = ':' # init string
    serializeNode = serializeNode + root.val
    serializeNode = serializeNode + ',' 
    serializeNode = serializeNode + root.left.val 
    # check to make sure there is not deeper node in our data
    if root.left.left | root.left.right:
        # build contionue to build our string
    serializeNode = serializeNode + ',' 
    serializeNode = serializeNode + root.right.val 
    # check to make sure there is not deeper node in our data
    if root.right.left | root.right.right:
        # build contionue to build our string
    serializeNode = serializeNode + ':'
    return serializeNode

def deserialize(nodeAsString):
    # define our variables that we want to deserialize
    i = 0
    onode = Node
    onode.val = ''
    # get our val
    while nodeAsString[i] != ',':
        onode.val += nodeAsString[i]
        if i == ':'
            # deserialize the node until we hit another ':'
        i += 1
    # add to go past our comma
    i += 1
    # get our left
    while nodeAsString[i] != ',':
        onode.val += nodeAsString[i]
        if i == ':'
            # deserialize the node until we hit another ':'
        i += 1
    # add to go past our comma
    i += 1
    # get our right
    while i in range(len(nodeAsString)):
        onode.val += nodeAsString[i]
        if i == ':'
            # deserialize the node until we hit another ':'
        i += 1
    # then return the string as a node class, deserializing it
    return onode

# The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'