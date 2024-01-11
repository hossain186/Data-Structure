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

    def search(self, target_data):

        current = self.head

        '''while current and current.data != target_data:

            current = current.next

        if not current: return  False

        return True'''

        while current!= None:

            if current.data == target_data:
                return True

            current = current.next

        return False


node = LinkedList()

node.push(388)
node.push(90)
node.push(100)
node.push(200)


print(node.search(200))




