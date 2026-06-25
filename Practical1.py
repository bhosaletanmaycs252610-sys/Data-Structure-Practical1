class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"'{item}' pushed into stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print(f"'{self.items.pop()}' removed from stack.")

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Top element:", self.items[-1])

    def size(self):
        print("Size of stack:", len(self.items))

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack:", self.items)

    def update(self, old, new):
        if old in self.items:
            index = self.items.index(old)
            self.items[index] = new
            print(f"'{old}' updated to '{new}'.")
        else:
            print("Element not found.")


stack = Stack()

while True:
    print("\n--- STACK ADT MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Update")
    print("6. Check Empty")
    print("7. Size")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element: ")
        stack.push(item)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        old = input("Enter element to update: ")
        new = input("Enter new value: ")
        stack.update(old, new)

    elif choice == 6:
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == 7:
        stack.size()

    elif choice == 8:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
