# class Stack:
#     def __init__(self):
#         self.size = 1000001
#         self.arr = [None] * self.size
#         self.top = -1

#     def push(self, element):
#         if self.size - self.top > 1:
#             self.top += 1
#             self.arr[self.top] = element
#         else:
#             print("Stack overflow")

#     def pop(self):
#         if self.top >= 0:
#             self.top -= 1
#         else:
#             print("Stack underflow")

#     def peek(self):
#         if self.top >= 0:
#             return self.arr[self.top]
#         else:
#             print("Stack is empty")
#             return -1

#     def is_empty(self):
#         return self.top == -1


# def tack_main():
#     st = Stack()
#     print("Select the operation you want to do: ")
#     while True:
#         print("1. For push operation.")
#         print("2. For pop operation.")
#         print("3. For peek operation.")
#         print("4. For checking stack is empty or not.")
#         print("Enter 4 to exit")
#         choice = input()
#         if choice == '4':
#             break
#         if choice == '1':
#             x = int(input("Enter the number you want to insert: "))
#             st.push(x)
#             print_list(head)
#         elif choice == '2':
#             pos = int(input("Enter the position: "))
#             head, tail = insert_at_position(head, tail, x, pos)
#             print_list(head)
#         elif choice == '3':
#             tail = insert_at_tail(tail, x)
#             print_list(head)
#         else:
#             print("Invalid! Enter a valid choice.")

    
