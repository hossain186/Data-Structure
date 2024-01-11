class Node:

    def __init__(self,data):

        self.data = data
        self.next = None


class LinkedList:


    def __init__(self):

        self.head = None


    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    #count node

    def countNode(self,h):

        current = h

        if not current: return 0

        return 1+ self.countNode(current.next)





nums = [1,2,3,4,5,6]
node = LinkedList()

for i in nums:
    node.push(i)

print(node.countNode(node.head))
