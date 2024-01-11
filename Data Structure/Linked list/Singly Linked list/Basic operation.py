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

    def display(self):

        current = self.head

        while current is not None:

            print(current.data, end="-->>")

            current = current.next
    def remove(self, data):

        current = self.head

        if current.data == data:

            self.head = current.next
            return
        prev = None

        while current and current.data != data:

            prev = current

            current = current.next


        if not current:
            return "No such element"
        prev.next = current.next
    def search(self, target):

        current = self.head
        c = 0
        while current and current is not Node:

            if  current.data == target: return f"Index to target element {c}"

            current = current.next

            c+=1


        return False

node = LinkedList()

node.append(100)
node.append(293)


print(node.search(100))

node.display()

