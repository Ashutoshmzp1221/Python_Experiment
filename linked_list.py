class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def remove_list(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
def linked_main():
    list = linkedList()
    print("-------------Linked List Operation-------------")
    print("Select a choice : ")
    print("1. For insert an element.")
    print("2. For removing an element.")
    print("3. To exit the program.")
    while True:
        choice = int(input("Enter choice: "))
        if choice == 1:
            x = int(input("\nEnter the number you want to insert: "))
            list.insert_at_head(x)
            list.print_list()
        elif choice == 2:
            list.remove_list()
        elif choice == 3:
            print("Exiting linked list!")
            break
        else:
            print("Invalid")
