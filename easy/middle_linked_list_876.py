from collections import deque


# https://leetcode.com/problems/moving-average-from-data-stream/description/
# https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1368/
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0
        self.count = 0

    def calc_avg(self) -> float:
        sum = 0
        for val in self.window:
            sum += val
        return sum / self.count

    def next(self, val: int) -> float:
        if self.count == self.size:
            # shift window along one
            self.window_sum -= self.window.popleft()
            self.count -= 1

        self.window.append(val)
        self.count += 1
        self.window_sum += self.window[-1]

        return self.window_sum / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
