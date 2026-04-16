import collections
from collections import Counter
from typing import List, Optional


#from requests.utils import from_key_val_list



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 1：给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
    # 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right - left) // 2 + left
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值target的那两个整数，
#并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictArr = {}
        for i, num in enumerate(nums):
            if num not in dictArr:
                dictArr[num] = i
        for i, num in enumerate(nums):
            if target - num in dictArr and dictArr[target - num] != i:
                return [dictArr[target - num], i]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        dictArr = {}
        for i, num in enumerate(nums):
            if target - num in dictArr:
                return [dictArr[target-num],i]
            dictArr[num] = i


#给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 解释：
# 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
# 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listParent = []
        listReturn = []
        for i, str in enumerate(strs):
            dictArr = {}
            listReturnChild = []
            flag = False
            for ch in str:
                if ch not in dictArr:
                    dictArr[ch] = 1
                else:
                    dictArr[ch] += 1

            for i, ch in enumerate(listParent):
                if ch == dictArr:
                    list = listReturn[i]
                    list.append(str)
                    flag = True
                    break
            if flag:
                continue
            listParent.append(dictArr)
            listReturnChild.append(str)
            listReturn.append(listReturnChild)
        return listReturn

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：
# 输入：nums = [1,0,1,2]
# 输出：3
 #   0 1 3 4 5
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums.sort()
        nums = sorted(set(nums))
        len = 0
        maxLen = 0
        beforeNum = 0
        for i, num in enumerate(nums):
            if i == 0:
                beforeNum = num
                len += 1
                maxLen = len
                continue
            if beforeNum + 1 == num:
                len += 1
                if len > maxLen:
                    maxLen = len
            else:
                if len - 1 != 0:
                    len = 1
            beforeNum = num
        return maxLen

    def longestConsecutive1(self, nums: List[int]) -> int:
        numsSet = set(nums)
        len_max = 0
        for e in numsSet:
            if e - 1 not in numsSet:
                current_len = 1
                current_value = e
                while current_value + 1 in numsSet:
                    current_len += 1
                    current_value += 1
                if current_len > len_max:
                    len_max = current_len
        return len_max


#     给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:
# 输入: nums = [0]
# 输出: [0]
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while left < right:
            if len(nums) < 2:
                break
            if right > len(nums) - 1:
                break
            if nums[left] == 0 and nums[right] == 0:
                right += 1
                continue
            if nums[left] == 0 and nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
            left += 1
            right += 1
        print(nums)

    def moveZeroes1(self, nums: List[int]) -> None:
        slow_pointer = 0
        for i, num in enumerate(nums):
            if num != 0:
                p = nums[slow_pointer]
                nums[slow_pointer] = num
                nums[i] = p
                slow_pointer += 1
        print(nums)
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例 2：
# 输入：height = [1,1]
# 输出：1
    def maxArea(self, height: List[int]) -> int:
        #实际就是求 索引距离*数组值 的两个元素最大值
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            area_value = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            max_area = max(max_area, area_value)
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area
        #解法111
        # max_area = 0
        # left_pointer = 0
        # right_pointer = 1
        # index_area = 1
        # while left_pointer < len(height) - 1:
        #     max_area = max(max_area, (min(height[right_pointer], height[left_pointer])) * index_area)
        #     if right_pointer < len(height) - 1:
        #         right_pointer += 1
        #         index_area += 1
        #         continue
        #     else:
        #         left_pointer += 1
        #         right_pointer = left_pointer + 1
        #         index_area = 1
        # return max_area

        #解法222
        # max_area = 0
        # for i, e in enumerate(height):
        #     for loop in range(1, len(height)):
        #         if (loop - i) * min(height[loop], e) > max_area:
        #             max_area = (loop - i) * min(height[loop], e)
        # return max_area

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return res

# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        dict_arr = {}
        for i, e in enumerate(s):
            k = i
            arr_len = 0
            while k <= len(s) - 1:
                if s[k] not in dict_arr:
                    dict_arr[s[k]] = 1
                    arr_len += 1
                    k += 1
                    max_len = max(max_len, arr_len)
                else:
                    dict_arr.clear()
                    break
        return max_len

    def lengthOfLongestSubstring1(self, s: str) -> int:
        max_len = 0
        set_arr = set()
        curr_len = 0
        left = 0
        for i, e in enumerate(s):
            curr_len += 1
            while e in set_arr:
                set_arr.remove(s[left])
                left += 1
                curr_len -= 1
            max_len = max(max_len, curr_len)
            set_arr.add(e)
        return max_len
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cn_p = Counter(p)
        cn_s = Counter()
        ans = []
        for i, e in enumerate(s):
            cn_s[e] += 1
            left = i + 1 - len(p)
            if left < 0:
                #未到窗口长度
                continue
            if cn_s == cn_p:
                ans.append(left)
            #右移左窗口
            cn_s[s[left]] -= 1
        return ans
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         dict_arr = {}
#         count = 0
#         for i, num in enumerate(nums):
#             dict_arr[num] = dict_arr.get(num, 0) + 1
#             if
    #前缀和+哈希表
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        count = 0
        mp = {0: 1}

        for num in nums:
            pre_sum += num
            count += mp.get(pre_sum - k, 0)
            mp[pre_sum] = mp.get(pre_sum, 0) + 1

        return count
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        mur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            mur = max(mur, cur)
        return mur
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 示例 3：
# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return_arr = []
        index_flag = []
        swap_index = []
        for i, interval in enumerate(intervals):
            if i in index_flag:
                continue
            flag = False

            for j in range(i + 1, len(intervals)):
                if (intervals[j][0] <= intervals[i][1] and intervals[j][0] >= intervals[i][0]
                        and intervals[j][1] >= intervals[i][1]):
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[i][0], intervals[j][1]] not in return_arr:
                        return_arr.append([intervals[i][0], intervals[j][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[i][0],intervals[j][1]]
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[j][0],intervals[i][1]] not in return_arr:
                        return_arr.append([intervals[j][0], intervals[i][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[j][0],intervals[i][1]]
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[j][0],intervals[j][1]] not in return_arr:
                        return_arr.append([intervals[j][0], intervals[j][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[j][0],intervals[j][1]]
                elif intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                    if i in swap_index:
                        return_arr.pop()
                    if [intervals[i][0],intervals[i][1]] not in return_arr:
                        return_arr.append([intervals[i][0], intervals[i][1]])
                    flag = True
                    index_flag.append(j)
                    swap_index.append(i)
                    intervals[i] = [intervals[i][0],intervals[i][1]]
                else:
                    continue
            if not flag:
                return_arr.append([intervals[i][0],intervals[i][1]])
        return return_arr

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i, interval in enumerate(intervals):
            if len(res) == 0:
                res.append(interval)
                continue
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max([res[-1][1], intervals[i][1]])
        return res
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = [0] * len(nums)
        for i, num in enumerate(nums):
            new_nums[(i+k) % len(nums)] = num
        nums[:] = new_nums
        print(nums)
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        k = k % lenth
        def reverse(left: int, right: int, nums: List[int]) -> None:
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        nums.reverse()
        reverse(0, k-1, nums)
        reverse(k, len(nums)-1, nums)

# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenth = len(nums)
        arr = [1] * len(nums)
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)
        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i - 1] * nums[i - 1]
        for i in range(lenth-2, -1, -1):
            right_arr[i] = right_arr[i+1] * nums[i+1]
        for i in range(lenth):
            arr[i] = left_arr[i] * right_arr[i]
        return arr
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 示例 1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range (1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit
        #
        # max_profit = 0
        # for i, price in enumerate(prices):
        #     j = i + 1
        #     while j < len(prices):
        #         max_profit = max(max_profit, prices[j] - price)
        #         j += 1
        # return max_profit
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false
# 示例 1：
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标
# 示例 2：
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标
    def canJump(self, nums: List[int]) -> bool:
        sum_value = 0
        for i in range(len(nums)):
            if i > sum_value:
                return False
            sum_value = max(sum_value, i + nums[i])
        return True
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：
# 0 <= j <= nums[i] 且
# i + j < n
# 返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。
# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2

    def jump(self, nums: List[int]) -> int:
        step = 0
        sum_value = 0
        default_index = 0
        if len(nums) <= 1:
            return sum_value
        for i in range(len(nums) - 1):
            sum_value = max(sum_value, i + nums[i])
            if i == default_index:
                step += 1
                default_index = sum_value
        return step
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，
# 但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
# 返回一个表示每个字符串片段的长度的列表。
# 示例 1：
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
# 示例 2：
# 输入：s = "eccbbbbdec"
# 输出：[10]
    def partitionLabels(self, s: str) -> List[int]:
        dict_arr = {s[0]:1}
        return_arr = []
        start = 0
        for i in range(1, len(s)):
            flag = False
            if s[i] in dict_arr:
                dict_arr[s[i]] += 1
                continue
            for j in range(i+1, len(s)):
                if s[j] in dict_arr:
                    flag = True
                    break
            if not flag:
                return_arr.append(i - start)
                start = i
                dict_arr.clear()
            dict_arr[s[i]] = 1
        return_arr.append(len(s) - start)
        return return_arr

    def partitionLabels1(self, s: str) -> List[int]:
        dict_arr = {}
        return_arr = []
        start = 0
        end = 0
        for i in range(len(s)):
            dict_arr[s[i]] = i
        for i in range(len(s)):
            end = max(end, dict_arr[s[i]])
            if end == i:
                return_arr.append(end - start + 1)
                start = i + 1
        return return_arr

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 示例 1：
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 示例 2：
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for i in range(3, n+1):
            temp = a
            a = b
            b = temp + b
        return b
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和
# 示例 1:
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 示例 2:
# 输入: numRows = 1
# 输出: [[1]]
    def generate(self, numRows: int) -> List[List[int]]:
        # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        dp = [] * numRows
        for i in range(numRows):
            dp_child = [0] * (i + 1)
            dp.append(dp_child)
        dp[0][0] = 1
        dp[1][0] = 1
        dp[1][1] = 1
        for i in range(2, numRows):
            for j in range(0, i + 1):
                if j == 0:
                    dp[i][j] = 1
                elif j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp

    def generate1(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp.append(row)
        return dp
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 示例 1：
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。

    def rob(self, nums: List[int]) -> int:
        '''
        偷第i家
        不偷第i家

        若偷第i家则   最大就是 dp = dp[i-2] + nums[i]
        若不偷第i家则 最大就是 dp = dp[i-1]
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        [1,2,3,1]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 4
        :pa`ram nums:
        :return:
        '''
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
# 给你一个整数 n ，返回和为 n 的完全平方数的最少数量
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是
# 示例 1：
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
# 示例 2：
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1
# 你可以认为每种硬币的数量是无限的。
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[i]表示总金额i所需最少硬币个数
        dp[0] = 0
        dp[i] = min(dp[i], dp[i - j] + 1)
        :param coins:
        :param amount:
        :return:
        '''
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for con in coins:
                if i - con >= 0:
                    dp[i] = min(dp[i], dp[i - con] + 1)
        if dp[amount] == float('inf'):
            dp[amount] = -1
        return dp[amount]
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp[i] = dp[]
        :param s:
        :param wordDict:
        :return:
        '''
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
# 示例 1:
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            midd = (right - left) // 2 + left
            if nums[midd] == target:
                return midd
            elif nums[midd] < target:
                left = midd + 1
            elif nums[midd] > target:
                right = midd - 1
        return left
# 给你一个满足下述两条属性的 m x n 整数矩阵：
# 每行中的整数从左到右按非严格递增顺序排列
# 每行的第一个整数大于前一行的最后一个整数
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            if target == num:
                return True
            elif target > num:
                left = mid + 1
            else:
                right = mid - 1
        return False
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置
# 如果数组中不存在目标值 target，返回 [-1, -1]
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            index = len(nums)
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] >= target:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        left_index = search(nums, target)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        right_index = search(nums, target+1) - 1
        return [left_index, right_index]

        # return_arr = [-1,-1]
        # if len(nums) == 1 and nums[0] == target:
        #     return_arr = [0, 0]
        #     return return_arr
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return_arr[0] = i
        #         flag = True
        #         while flag:
        #             if nums[i] == target and i < len(nums) - 1:
        #                 return_arr[1] = i
        #                 i += 1
        #             else:
        #                 flag = False
        #         return return_arr
        # return return_arr
        # return_arr = []
        # left = 0
        # right = len(nums) - 1
        # flag = False
        # while left <= right:
        #     midd = (right - left) // 2 + left
        #         if nums[midd] == target:
        #             flag = True
# 整数数组 nums 按升序排列，数组中的值 互不相同
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标从0开始计数）
# 例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0    [0 1 2 4 5 6 7] index= 3
# 输出：4
# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
# 输入：nums = [1], target = 0
# 输出：-1
    def search1(self, nums: List[int], target: int) -> int:






        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        index = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                index = i
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                if mid > index:
                    return mid - index
                else:
                    return mid + index + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

#给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        arr = set()
        while headA:
            arr.add(headA)
            headA = headA.next
        while headB:
            if headB in arr:
                return headB
            else:
                headB = headB.next
        return None

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left = headA
        right = headB
        while left != right:
            left = left.next if left else headB
            right = right.next if right else headA
        return left



    #给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0)
        while head:
            if new_head.next:
                temp = new_head.next
                new_head.next = ListNode(head.val)
                new_head.next.next = temp
            else:
                new_head.next = ListNode(head.val)
            head = head.next
        return new_head.next

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        he = head
        while he:
            temp = he.next
            he.next = prev
            prev = he
            he = temp
        return prev
#给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def compareNode(head1: ListNode, head2: ListNode) -> bool:
            while head1:
                if head1.val != head2.val:
                    return False
                else:
                    head1 = head1.next
                    head2 = head2.next
            return True
        prev = None
        he = head

        dummy = ListNode(1)
        head_temp = dummy
        while head:
            head_temp.next = ListNode(head.val)
            head_temp = head_temp.next
            head = head.next
        while he:
            temp = he.next
            he.next = prev
            prev = he
            he = temp
        return compareNode(prev, dummy.next)

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        #链表反转
        prev= None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        p1 = head
        p2 = prev
        while p2:
            if p2.val != p1.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
# 给你一个链表的头节点 head ，判断链表中是否有环
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况
# 如果链表中存在环 ，则返回 true 。 否则，返回 false
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = set()
        while head:
            if head in arr:
                return True
            else:
                arr.add(head)
            head = head.next
        return False

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# 给定一个链表的头节点head ，返回链表开始入环的第一个节点。 如果链表无环，则返回null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况,不允许修改链表
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = set()
        while head:
            if head in arr:
                return head
            else:
                arr.add(head)
            head = head.next
        return None

# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

s = Solution()

hea1 = ListNode(1)
hea2 = ListNode(2)
hea3 = ListNode(2)
hea4 = ListNode(1)
hea1.next = hea2
hea2.next = hea3
hea3.next = hea4
flag = s.isPalindrome(hea1)
print(flag)
# hea1 = ListNode(1)
# hea2 = ListNode(2)
# hea3 = ListNode(3)
# hea4 = ListNode(4)
# hea5 = ListNode(5)
# hea1.next = hea2
# hea2.next = hea3
# hea3.next = hea4
# hea4.next = hea5
# node_new = s.reverseList(hea1)
# print(node_new)
# common1 = ListNode(8)
# common2 = ListNode(4)
# common3 = ListNode(5)
# common1.next = common2
# common2.next = common3
#
# nodeA1 = ListNode(4)
# nodeA2 = ListNode(1)
# nodeA1.next = nodeA2
# nodeA2.next = common1
#
# nodeB1 = ListNode(5)
# nodeB2 = ListNode(6)
# nodeB1.next = nodeB2
# nodeB2.next = common1
# val = s.getIntersectionNode1(nodeA1, nodeB1)
# print(val)


# index = s.search1([4,5,6,7,0,1,2], 3)
# print(index)
#arr = s.searchRange([5,7,7,8,8,10], 8)
#arr = s.searchRange([5,7,7,8,8,10], 6)
#print(arr)
#flag = s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
# flag = s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
# print(flag)
# index = s.searchInsert([1,3,5,6],7)
# print(index)
#num = s.coinChange([1, 2, 5], 11)
#num = s.coinChange([2], 3)
# num = s.coinChange([1], 0)
# print(num)
# s = 3
# print(s // 2)
# num = s.numSquares(13)
# print(num)
#num = s.rob([1,2,3,1])
#num = s.rob([2,7,9,3,1])
#print(num)
# arr = s.generate1(5)
# print(arr)
# time = s.climbStairs1(4)
# print(time)
#arr = s.partitionLabels1("ababcbacadefegdehijhklij")
#arr = s.partitionLabels1("eccbbbbdec")
#print(arr)
#num = s.jump([2,3,1,1,4])
#num = s.jump([2,3,0,1,4])
#num = s.jump([1,2,1,1,1])
# num = s.jump([1,2])
# print(num)
#flag = s.canJump([2,3,1,1,4])
#flag = s.canJump([3,2,1,0,4])
#flag = s.canJump([0])
#print(flag)
#max_value = s.maxProfit([7,1,5,3,6,4])
#max_value = s.maxProfit([7,6,4,3,1])
#print(max_value)
# arr = s.productExceptSelf([1,2,3,4])
# print(arr)
#s.rotate1([1,2,3,4,5,6,7], 3)
#s.rotate1([-1], 2)

#intervals = [[1,3],[2,6],[8,10],[15,18]]
#intervals = [[1,4],[4,5]]
#intervals = [[4,7],[1,4]]
#intervals = [[1,4],[2,3]]
#intervals = [[1,4],[0,2],[3,5]]
# intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
# arr = s.merge1(intervals)
# print(arr)
#len = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#len = s.maxSubArray([1])
#len = s.maxSubArray([5,4,-1,7,8])
#print(len)
#num = s.subarraySum([1,1,1], 2)
#num = s.subarraySum([1,2,3], 3)
#num = s.subarraySum([1], 0)
#num = s.subarraySum([1, 3, 5, 4], 9)
#print(num)
# arr = s.findAnagrams("cbaebabacd", "abc")
# print(arr)
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]

# s = "cbaebabacd"
# p = "abc"
# dict_arr = Counter(p)
# print(dict_arr)
# arr = Counter()
# print(arr)
#len = s.lengthOfLongestSubstring("abcabcbb")
#len = s.lengthOfLongestSubstring("pwwkew")
#len = s.lengthOfLongestSubstring1(" ")
#len = s.lengthOfLongestSubstring("c")
#print(len)
#arr = [1,8,6,2,5,4,8,3,7]
# arr = [4,3,2,1,4]
# #arr = [1,1]
# print(s.maxArea(arr))
# arr = s.threeSum([-1,0,1,2,-1,-4])
# print(arr)
# arr = [1,3,2,6]
# for loop in range(1, len(arr)):
#     print(loop)
#     print(arr[loop])

#s.moveZeroes([1,0,1])
#s.moveZeroes1([0,1,0,3,12])
# str = s.search1(nums=[6,7,8,9], target=9)
# print(str)

# arr = s.twoSum1([3,2,4], 6)
# print(arr)
# for i in range(0,10):
#     print(i)

# sttr = s.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(sttr)
# arr = [1,3,2,0]
# arr.sort()
# print(arr)
# len = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
# print(len)
#len = s.longestConsecutive([1,0,1,2])
#len = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
#len = s.longestConsecutive1([9,1,4,7,3,-1,0,5,8,-1,6])
#-1 0 1 3 4 5 6 7 8 9
#len = s.longestConsecutive([100,4,200,1,3,2])
#print(len)
# arr = [9,1,4,7,3,-1,0,5,8,-1,6]
# print(len(arr))