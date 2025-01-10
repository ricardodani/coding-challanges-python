from typing import List


class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order, remove some
    duplicates in-place such that each unique element appears at most twice.
    The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages,
    you must instead have the result be placed in the first part of the array
    nums.
    More formally, if there are k elements after removing the duplicates, then
    the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array.
    You must do this by modifying the input array in-place with O(1) extra
    memory.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        occurences = {}
        total_occurences = []

        for i, v in enumerate(nums):
            if v not in occurences:
                occurences[v] = 1 
                total_occurences.append(i)
            elif occurences[v] == 1:
                occurences[v] += 1
                total_occurences.append(i)

        for index, occurence_index in enumerate(total_occurences):
            nums[index] = nums[occurence_index]

        return len(total_occurences)


s = Solution()


def test_solution_case_1():
    nums = [1, 1, 1, 2, 2, 3]
    expected_nums = [1, 1, 2, 2, 3] 
    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == expected_nums


def test_solution_case_2():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected_nums = [0, 0, 1, 1, 2, 3, 3]
    assert s.removeDuplicates(nums) == 7
    assert nums[:7] == expected_nums

if __name__ == "__main__":
    test_solution_case_1()
    test_solution_case_2()