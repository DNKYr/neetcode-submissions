class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low = 0
        high = n - 1
        value = target - numbers[low]
        while value != numbers[high]:
            if value < numbers[high]:
                high -= 1
            elif value > numbers[high]:
                low += 1
                value = target - numbers[low]
        return [low + 1, high + 1]