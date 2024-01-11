class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None



    def append(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            return

        current = self.head

        while current.next is not None:

            current = current.next

        current.next= new_node


    # insert in first position

    def insertAtBiggening(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    #insert at end
    def insertAfterNode(self, data, prev_node):

        if not prev_node:
            print("No previous node found")
            return


        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node


    def insertAtEnd(self, data):

        new_node = Node(data)

        current = self.head

        while current.next is not None:

            current = current.next

        current.next = new_node




    def display(self):

        current = self.head

        while current is not None:

            print(current.data, end="-->>")

            current = current.next




nums = [100, 200,300,400]
node = LinkedList()

for i in nums:

    node.append(i)



node.insertAtBiggening(39)

node.insertAtEnd(1000)

node.insertAfterNode(10000, node.head.next.next.next)
node.display()


