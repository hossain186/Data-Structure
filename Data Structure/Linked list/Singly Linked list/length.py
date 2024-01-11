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

    #cout all Node

    def length(self):

        len = 0

        current = self.head

        while current!=None:

            len+=1
            current = current.next

        return len



nums = [1,2,3,4,5,6]
node = LinkedList()

for i in nums:
    node.push(i)

print("Count of node is",node.length(), sep=" = ")




