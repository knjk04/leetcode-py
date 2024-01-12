# https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1368/
# https://leetcode.com/problems/moving-average-from-data-stream/description/
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []

    def calc_avg(self) -> float:
        sum = 0
        for val in self.window:
            sum += val
        return sum / len(self.window)

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            # shift window along one
            self.window = self.window[1:]
        self.window.append(val)
        return self.calc_avg()

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
