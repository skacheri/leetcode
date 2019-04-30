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

# 69. Sqrt (x)

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid -1
        if end * end < x:
            return end
        else:
            return start

################################################################################

# 70. Climbing Stairs

class Solution(object):
    def __init__(self):
        self.dic = {1:1, 2:2}
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

################################################################################

# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        current = head
        while current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head

################################################################################

# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, (m+n)-1
        while j > -1 and i > -1:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        if i < 0:
            while j > -1:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

################################################################################

# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p != None and q != None:
            if p.val == q.val and self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left):
                return True
        return False

################################################################################

# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, t1, t2):
        if (t1 and not t2) or (t2 and not t1):
            return False
        elif not t1 and not t2:
            return True
        else:
            return self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left) and t1.val == t2.val

################################################################################

# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        output = []
        if not root: # first take care of edge case if they hand you an empty tree
            return []
        queue.append(root)
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                seeing = queue.pop(0)
                level.append(seeing.val)
                if seeing.left:
                    queue.append(seeing.left)
                if seeing.right:
                    queue.append(seeing.right)
            output.append(level)
        return output
                

################################################################################

# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            max_depth_left = self.maxDepth(root.left)
            max_depth_right = self.maxDepth(root.right)
        return max(max_depth_left, max_depth_right) +1

################################################################################

# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        output = []
        queue.append(root)
        if not root:
            return []
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                seeing = queue.pop(0)
                level.append(seeing.val)
                if seeing.left:
                    queue.append(seeing.left)
                if seeing.right:
                    queue.append(seeing.right)
            output.append(level)
        
        return output[::-1]

################################################################################

# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        if root.right == None and root.left != None:
            return self.minDepth(root.left) + 1
        else:
            depth_left = self.minDepth(root.left)
            depth_right = self.minDepth(root.right) 
            return min(depth_left, depth_right) + 1

################################################################################

# 125. 

################################################################################


################################################################################

################################################################################

################################################################################

################################################################################

# 541. Reverse String II

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = list(s)
        for i in range(0, len(s), 2*k):
            rev = s[i:i+k]
            result[i:i+k] = rev[::-1]
        return "".join(result)

################################################################################

# 796. Rotate String

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        A2 = A+A
        if B in A2:
            return True
        return False

################################################################################

# 806. Number of Lines To Write String

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        dct = {}
        for char in range(26):
            dct[chr(char+97)] = widths[char]
        summ = 0
        line = 0
        for char in S:
            if summ + dct[char] <= 100:
                summ += dct[char]
            else:
                line += 1
                summ = dct[char]
        return [line+1, summ]

################################################################################

# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = 0
        stack1 = []
        stack2 = []
        
        while i < len(S):
            if S[i] == "#":
                if stack1:
                    stack1.pop()
                i += 1
            else:
                stack1.append(S[i])
                i += 1
        i = 0        
        while i < len(T):
            if T[i] == "#":
                if stack2:
                    stack2.pop()
                i += 1
            else:
                stack2.append(T[i])
                i += 1
            
        if stack1 == stack2:
            return True
        return False

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



