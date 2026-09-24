class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        pt1 = 0
        pt2 = n - 1
        while True:
            addition = numbers[pt1] + numbers[pt2]
            if addition == target:
                return [pt1+1, pt2+1]
            elif addition < target:
                pt1 += 1
            else:
                pt2 -= 1