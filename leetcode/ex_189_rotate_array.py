from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k = k % nums_len if nums_len > k else k
        for i, v in enumerate(nums[nums_len-k:nums_len] + nums[:nums_len-k:]):
            nums[i] = v


s = Solution()


def test_solution_case_1():
    nums = [1,2,3,4,5,6,7]
    k = 3
    expected_result = [5,6,7,1,2,3,4]
    assert s.rotate(nums, k) == expected_result 


def test_solution_case_2():
    nums = [-1,-100,3,99]
    k = 2
    expected_result = [3,99,-1,-100]
    assert s.rotate(nums, k) == expected_result 

if __name__ == "__main__":
    test_solution_case_1()
    test_solution_case_2() 