import collections
from typing import List


class Solution:

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，
# 并返回它们的数组下标。你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = dict()
        return_arr = []
        for i in range(len(nums)):
            if target - nums[i] in arr:
                #arr.get()
                return_arr.append(arr.get(target - nums[i]))
                return_arr.append(i)
                return return_arr
            else:
                arr[nums[i]] = i
    # 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for i in range(len(strs)):
            mp[''.join(sorted(strs[i]))].append(strs[i])
        return list(mp.values())
        # arr = []
        # index_arr = set()
        # for i in range(len(strs)):
        #     if i in index_arr:
        #         continue
        #     child = []
        #     dict_sort = sorted(strs[i])
        #     child.append(strs[i])
        #     for j in range(i+1, len(strs)):
        #         if j in index_arr:
        #             continue
        #         if sorted(strs[j]) == dict_sort:
        #             child.append(strs[j])
        #             index_arr.add(j)
        #     arr.append(child)
        # return arr
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        max_len = 1
        len_child = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                len_child += 1
            else:
                len_child = 1
            max_len = max(max_len, len_child)
        return max_len
    def longestConsecutive1(self, nums: List[int]) -> int:
        set_arr = set(nums)
        max_len = 0
        for num in set_arr:
            if num - 1 not in set_arr:
                cur_len = 1
                cur_value = num
                while cur_value + 1 in set_arr:
                    cur_len += 1
                    cur_value += 1
                max_len = max(max_len, cur_len)
        return max_len
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums) - 2):
            if i >0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    arr.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return arr










s = Solution()

nums = [-1,0,1,2,-1,-4]
arr = s.threeSum(nums)
print(arr)
# he = s.maxArea([1,8,6,2,5,4,8,3,7])
# print(he)
# nums = [0,1,0,3,12]
# s.moveZeroes(nums)

#nums = [100,4,200,1,3,2]
#nums = [0,3,7,2,5,8,4,6,0,1]
#nums = [1,0,1,2]
# l = len(nums)
# print(l)
# length = s.longestConsecutive1(nums)
# print(length)
# arr = s.twoSum(nums=[2, 7, 11, 15], target=9)
# print(arr)




# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# arr = s.groupAnagrams(strs)
# print(arr)
# print(mp)
# print(sorted("eat"))