class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_at_head(head, x):
    temp = Node(x)
    temp.next = head
    return temp

def insert_at_tail(tail,x):
    temp = Node(x)
    tail.next = temp
    return temp

def insert_at_position(head,tail,x,pos):
    if(pos <= 1):
        return insert_at_head(head,x),tail
    else:
        temp = head
        t = pos - 2
        while t and temp.next:
            t -= 1
            if temp.next:
                P = Node(x)
                P.next = temp.next
                temp.next = P
            else:
                return insert_at_tail(head,x)
            return head, tail

def size_link(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    return count

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
def main():
    print("-------------Linked List Operation-------------")
    temp = Node(10)
    head = temp
    tail = head
    head = insert_at_head(head, 15)
    print_list(head)

    while True:
        print("Enter the position at which you want to insert:")
        print("Enter 1 to insert at the head")
        print("Enter 2 to insert at any position")
        print("Enter 3 to insert at the tail")
        print("Enter 4 to exit")
        choice = input()
        if choice == '4':
            break
        x = int(input("Enter the number you want to insert: "))
        if choice == '1':
            head = insert_at_head(head, x)
            print_list(head)
        elif choice == '2':
            pos = int(input("Enter the position: "))
            head, tail = insert_at_position(head, tail, x, pos)
            print_list(head)
        elif choice == '3':
            tail = insert_at_tail(tail, x)
            print_list(head)
        else:
            print("Invalid! Enter a valid choice.")

