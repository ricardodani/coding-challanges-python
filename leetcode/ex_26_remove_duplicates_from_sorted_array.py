from typing import List, Any

_ = "_"

class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted,
    you need to do the following things:

    Change the array nums such that the first k elements of nums contain the
    unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size of nums.

    Return k.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        occurences = {}

        for i, v in enumerate(nums):
            if not v in occurences:
                occurences[v] = i

        for current_index, index in enumerate(occurences.values()):
            nums[current_index] = nums[index]

        return len(occurences)


s = Solution()


def test_solution_case_1():
    nums = [1, 1, 2]
    expected_nums = [1, 2] 
    assert s.removeDuplicates(nums) == 2
    assert nums[:2] == expected_nums


def test_solution_case_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]
    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == expected_nums

if __name__ == "__main__":
    test_solution_case_1()
    test_solution_case_2()