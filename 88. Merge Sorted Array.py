class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #Do not return anything, modify nums1 in-place instead.

        # Get last index of nums1
        last = m + n - 1
        # Adjust m and n to be the last elements of their respective arrays
        n -= 1
        m -= 1

        # Merge in reverse order
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            # Decrement last regardless of which element was greater
            last -= 1

        # If there are leftover element in nums2
        while n >= 0:
            nums1[last] = nums2[n]
            last -= 1
            n -= 1

#time: O(n)
#space: O(1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution_instance = Solution()
solution_instance.merge(nums1, m, nums2, n)
print(nums1)