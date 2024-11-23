class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def add_num(self, num):
        if not self.left or num <= -self.left[0]:
            self.left.append(-num)
            self.left.sort(reverse=True)
        else:
            self.right.append(num)
            self.right.sort()

        if len(self.left) > len(self.right) + 1:
            self.right.append(-self.left.pop(0))
            self.right.sort()
        elif len(self.right) > len(self.left):
            self.left.append(-self.right.pop(0))
            self.left.sort(reverse=True)

    def find_median(self):
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        return -self.left[0]


def calculate_median_stream(nums):
    median_finder = MedianFinder()
    medians = []

    for num in nums:
        median_finder.add_num(num)
        medians.append(median_finder.find_median())

    return medians


nums = [5, 4, 1, 7, 2, 6]
print(calculate_median_stream(nums))
