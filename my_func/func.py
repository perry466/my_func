class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        测试代码
        from my_func.func import Solution

        sol = Solution()
        result = sol.twoSum([2, 7, 11, 15], 9)
        print(result)


        """
        hash_map = dict()
        for idx,num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement],idx]
            hash_map[num] = idx