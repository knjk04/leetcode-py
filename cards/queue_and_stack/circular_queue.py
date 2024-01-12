class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.start_pos = None
        self.end_pos = None
        print(f"Initialised queue of size: {k}\n")

    def enQueue(self, value: int) -> bool:
        print(f"Enqueue: {value}...")

        if self.isFull():
            print()
            return False

        if self.end_pos is not None and (
                self.end_pos + 1 == self.size or self.end_pos < self.start_pos):
            # circular queue
            self.end_pos = 0
            self.queue.insert(0, value)
            print(f"Post end pos={self.end_pos}")
            return True

        print(f"Pre enqueue queue: {self.queue}")
        self.queue.append(value)

        if self.isEmpty():
            print("initialising start and end")
            self.start_pos = self.end_pos = 0

        elif self.end_pos is not None:
            # cannot use 'elif self.end_pos' because 0 is not truthy
            self.end_pos += 1
            print(f"Pre end pos={self.end_pos}")
            # keep within the bounds of the fixed-sized list
            self.end_pos %= self.size
            print(f"Post end pos={self.end_pos}")

        print(f"Post enqueue queue: {self.queue}")
        print()
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue.pop(0)
        self.start_pos += 1
        # keep within the bounds of the fixed-sized list
        self.start_pos %= self.size

        if self.start_pos > self.end_pos:
            self.start_pos = self.end_pos = None

        print(f"Dequeue. Start pos = {self.start_pos}, queue:{self.queue}")
        print()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        front = self.queue[self.start_pos]
        print(f"Front of the queue: {front}")
        return front

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        print(f"Rear end_pos={self.end_pos}", sep=" ")
        rear = self.queue[self.end_pos]
        print(f"Rear of the queue: {rear}")
        return rear

    def isEmpty(self) -> bool:
        is_empty = self.start_pos == self.end_pos == None
        print(f"Is empty: {is_empty}")
        return is_empty

    def isFull(self) -> bool:
        # is_full = self.start_pos == 0 and self.end_pos == self.size-1

        if self.start_pos is None:
            return False

        # -1 because the indices are zero indexed
        is_full = self.end_pos - self.start_pos == self.size - 1
        print(
            f"Is full={is_full}, start pos={self.start_pos}, end_pos={self.end_pos}")
        return is_full

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
