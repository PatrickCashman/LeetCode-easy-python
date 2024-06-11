class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}

        # Count the frequencies of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        length = 0
        odd_found = False

        # Iterate over the character counts
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True

        # If there was any character with an odd count, we can add one odd character in the center
        if odd_found:
            length += 1

        return length

#time: O(n)
#space: O(1)

s = "abccccdd"
solution_instance = Solution()
print(solution_instance.longestPalindrome(s))