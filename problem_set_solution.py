# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(0, len(nums)):  
            num_list = dct.get(nums[i], list())
            num_list.append(i)
            dct[nums[i]] = num_list
        # print(dct)
        for i in range(len(nums)):
            if target-nums[i] in dct and target-nums[i] != nums[i]:
                return [i, dct[target-nums[i]][0]]
            elif target-nums[i] == nums[i]:
                if len(dct[nums[i]]) > 1:
                    return dct[nums[i]]
        return []

################################################################################

#7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x < (-2 ** 31) or x > ((2 ** 31) -1):
            return 0
        else:
            result = 0
            neg = False
            if x < 0:
                neg = True
                x = -1 * x
            while (x != 0):
                digit = x % 10
                x = x // 10
                result = result*10 + digit
                if result < (-2 ** 31) or result > ((2 ** 31) -1):
                    return 0
            if neg:
                return (-1 * result)
            return result

################################################################################

#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        i = 0
        y = str(x)
        j = len(y)-1
        while(i<=j):
            if y[i] == y[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

################################################################################

#13. Roman to Integer

