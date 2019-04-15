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

# 7. Reverse Integer

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

# 9. Palindrome Number

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

# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={"I":"1",
                    "V":"5",
                    "X":"10",
                    "L":"50",
                    "C":"100",
                    "D":"500",
                    "M":"1000"}
        set_units={"X","V"}
        set_tens={"L","C"}
        set_hundreds={"D","M"}
        sum_num = 0
        for idx in range(len(s)):
            if s[idx] in roman_dict:
                if idx<len(s)-1:
                    if s[idx]=="I" and s[idx+1] in set_units:
                        sum_num =sum_num -2
                    elif s[idx]=="X" and s[idx+1] in set_tens:
                        sum_num =sum_num -20
                    elif s[idx]=="C" and s[idx+1] in set_hundreds:
                        sum_num =sum_num -200
                sum_num = sum_num + int(roman_dict[s[idx]])
        return sum_num

################################################################################

# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def short_word(self, strs):
            shortest = len(strs[0])
            shortest_word = strs[0]
            for word in strs:
                if len(word)<shortest:
                    shortest_word = word
            return shortest_word
        
        short = short_word(self, strs)
        count = 0
        while(count<len(strs)):
            if (strs[count]).startswith(short): 
                count += 1
            else:
                short = short[:-1]
                count = 0
        return short

################################################################################

# 20. Valid Parenthesis

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {"(":")", "{":"}", "[":"]"}
        for bracket in s:
            if bracket in dct.keys():
                stack.append(dct[bracket])
            elif len(stack) != 0 and stack.pop() == bracket:
                continue
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

################################################################################

# 21. Merge Two Sorted Lsits

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        pointer = l3
        if l2 and not l1:
            return l2
        elif l1 and not l2:
            return l1
        elif not l1 and not l2:
            return None
        else:
            while l1 and l2:
                if l1.val <= l2.val:
                    pointer.next = l1
                    l1 = l1.next
                    pointer = pointer.next
                elif l2.val < l1.val:
                    pointer.next = l2
                    l2 = l2.next
                    pointer = pointer.next
            if l1 and not l2:
                pointer.next = l1
            if l2 and not l1:
                pointer.next = l2
        return l3.next

################################################################################

# 26. Remove Duplicates from Sorted Array 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return None
        i = 0
        j = 1
        while j <len(nums):
            if nums[i] == nums[j]:
                pass
            else:
                i = i + 1
                nums[i] = nums[j]
            j = j + 1
        return i+1

################################################################################

# 27. Remove Element  

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointers (algorithm)
        # i = 0
        # for j in range(0, len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        # return i
        #two pointers with rare values that match (algorithm)
        i = 0
        n = len(nums)
        while (i < n):
            if nums[i] == val:
                nums[i] = nums[n-1]
                n = n - 1
            else:
                i = i + 1
        return n

################################################################################

# 28. Implement strStr()   

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        len_needle = len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len_needle] == needle:
                        return i
        else:
            return -1

################################################################################

# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # print(mid, nums[mid], target)
        if nums[mid] > target:
            return mid
        else:
            return mid + 1

################################################################################

# 53. Maximum Subarray  

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return None
        max_seen = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev < 0:
                prev = nums[i]
            else:
                prev = prev + nums[i]
            if prev > max_seen:
                max_seen = prev
        return max_seen

################################################################################

# 58. Length of Last Word    

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s is "":
            return 0
        count = 0
        i = len(s)-1
        while s[i] != " " and i >= 0:
            count = count + 1
            i = i -1
        return count

################################################################################

# 66. Plus One 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 1
        for idx in range(len(digits)-1, -1, -1):
            number = carry_over + digits[idx]
            carry_over = 0
            carry_over = int(number / 10)
            if carry_over == 1:
                digits[idx] = number % 10
            else:
                digits[idx] = number
        if carry_over == 1:
            return [1] + digits
        else:
            return digits

################################################################################

# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        power = 0
        index = -1
        output = ""
        number = 0
        abs_index = -1 * index
        while (abs_index <= len(a)) and (abs_index <= len(b)):
            number = number + (2**power)*(int(a[index])) + (2**power)*(int(b[index]))
            power += 1
            index = index - 1
            abs_index = -1 * index
        if abs_index <= len(a) and abs_index > len(b):
            while(abs_index <= len(a)):
                number = number + (2**power)*(int(a[index]))
                index = index - 1
                abs_index = -1 * index
                power += 1
        else:
            while(abs_index <= len(b)):
                number = number + (2**power)*(int(b[index]))
                index = index - 1
                abs_index = -1 * index
                power += 1
        if number == 0:
            return "0"
        while number > 0:
            output = str(number % 2) + output
            number = number // 2
        return output

################################################################################

# 859. Buddy Strings

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        count = 0
        swap_a = []
        swap_b = []
        
        for a,b in zip(A, B):
            if a != b:
                count += 1
                swap_a.append(a)
                swap_b.append(b)
                # if count > 2:
                #     return False
        if count == 0:
            return len(set(A)) != len(A)
        elif count != 2:
            return False
        else:    
            return swap_a[::-1] == swap_b

################################################################################



