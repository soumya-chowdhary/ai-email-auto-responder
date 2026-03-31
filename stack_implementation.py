stack = []
def push(element):
    stack.append(element)
    print(element, "pushed into stack")
def pop():
    if is_empty():
        print("Stack is empty")
    else:
        print(stack.pop(), "popped from stack")
def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])
def is_empty():
    return len(stack) == 0
def display():
    print("Stack elements:", stack)
push(10)
push(20)
push(30)
display()
peek()
pop()
display()
