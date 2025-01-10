from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min_for_majority = len(nums) / 2
        occurences = {}
        for i, v in enumerate(nums):
            if v not in occurences:
                occurences[v] = 1
            else:
                occurences[v] += 1

            if occurences[v] > min_for_majority:
                return v


s = Solution()


def test_solution_case_1():
    nums = [3, 2, 3]
    expected_result = 3 
    assert s.majorityElement(nums) == expected_result 


def test_solution_case_2():
    nums = [2, 2, 1, 1, 1, 2, 2]
    expected_result = 2
    assert s.majorityElement(nums) == expected_result 

if __name__ == "__main__":
    test_solution_case_1()
    test_solution_case_2()