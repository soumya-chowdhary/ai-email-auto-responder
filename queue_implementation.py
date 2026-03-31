queue = []
def enqueue(element):
    queue.append(element)
    print(element, "inserted into queue")
def dequeue():
    if is_empty():
        print("Queue is empty")
    else:
        print(queue.pop(0), "removed from queue")
def front():
    if is_empty():
        print("Queue is empty")
    else:
        print("Front element is:", queue[0])
def is_empty():
    return len(queue) == 0
def display():
    print("Queue elements:", queue)
enqueue(5)
enqueue(15)
enqueue(25)
display()
front()
dequeue()
display()
