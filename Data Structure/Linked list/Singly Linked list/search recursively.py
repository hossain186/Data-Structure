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

    #search element

    def search(self,h, target_data):

        if h is None:   return False

        if h.data == target_data: return True

        return self.search(h.next, target_data)






node = LinkedList()

node.push(388)
node.push(90)
node.push(100)
node.push(200)


print(node.search(node.head, 2002))




