from typing import List

class Solution:

    def switch_with_next_match(self, nums, index, val):
        starting_from = index + 1
        for n in nums[starting_from:]:
            if n != val:
                nums[index], nums[starting_from] = nums[starting_from], nums[index]
                return

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n != val:
                k += 1
                self.switch_with_next_match(nums, i, val)
        return k


class TestSolution:
    def __init__(self):
        self.s = Solution()
    
    def test_all(self):
        self._test_remove_element_scenario_1()

    def _test_remove_element_scenario_1(self):
        array = [3, 2, 2, 3]
        assert self.s.removeElement(array, 3) == 2
        assert array[:2] == [2, 2]

if __name__ == '__main__':
    t = TestSolution()
    t.test_all()