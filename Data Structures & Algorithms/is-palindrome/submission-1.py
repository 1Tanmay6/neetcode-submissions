import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]'
        s = re.sub(pattern, '', s)
        s = s.lower()
        length_s = len(s)
        if length_s % 2 == 0:
            half_length = int(length_s/2)
            first_half = s[0: half_length]
            second_half = s[half_length: length_s]
            reverse_second_half = second_half[::-1]
            return first_half == reverse_second_half
        else:
            first_half = s[0: length_s//2]
            second_half = s[length_s//2+1: length_s]
            reverse_second_half = second_half[::-1]
            return first_half == reverse_second_half