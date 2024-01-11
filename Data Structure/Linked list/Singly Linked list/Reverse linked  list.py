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

    def display(self):

        current = self.head

        while current!=None:

            print(current.data, end="-->>")
            current = current.next

    def reverse_list(self):

        current = self.head

        previous = None

        while current!=None:

            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous







nums = [1,2,3,4,5,6]
node = LinkedList()

for i in nums:
    node.push(i)


node.display()
node.reverse_list()
print("\n")
node.display()