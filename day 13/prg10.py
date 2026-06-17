class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peekfront(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def peekrear(self):
        if not self.is_empty():
            return self.queue[-1]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []

d = queue()
d.enqueue(100)
d.enqueue(200)
d.enqueue(300)
d.enqueue(400)
d.enqueue(500)
print(d.dequeue())
print(d.peekfront())
print(d.peekrear())
print(d.is_empty())
d.clear()
print(d.is_empty())