from queue import Queue
q = Queue(maxsize = 3)
def que_main():
    print("-------------Queue Operation-------------")
    while True:
        print("Select the operation you want to do: ")
        print("1. For enqueue operation.")
        print("2. For dequeue operation.")
        print("3. Is queue is empty.")
        print("4.. For exiting the program")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            x = int(input("Enter the number you want to insert: "))
            q.put(x)
            print(f"Element {x} pushed onto the queue.")
        elif choice == 2:
            print("The dequed element is", q.get())
        elif choice == 3:
            if q.empty():
                print("The queue is empty.")
            else:
                print("Queue is not empty")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid choice.")
        print("\n")


