import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]'
        s = re.sub(pattern, '', s)
        s = s.lower()
        length_s = len(s)
        
        # solution 1
        # if length_s % 2 == 0:
        #     half_length = int(length_s/2)
        #     first_half = s[0: half_length]
        #     second_half = s[half_length: length_s]
        #     reverse_second_half = second_half[::-1]
        #     return first_half == reverse_second_half
        # else:
        #     first_half = s[0: length_s//2]
        #     second_half = s[length_s//2+1: length_s]
        #     reverse_second_half = second_half[::-1]
        #     return first_half == reverse_second_half


        # solution 2
        if length_s == 0:
            return True
        start_pointer = 0
        end_pointer = length_s - 1
        if length_s % 2 != 0:
            while start_pointer != end_pointer:
                if s[start_pointer] != s[end_pointer]:
                    return False
                start_pointer += 1
                end_pointer -= 1
            return True
        else:
            while True:
                if s[start_pointer] != s[end_pointer]:
                    return False
                if start_pointer + 1 == end_pointer:
                    break
                start_pointer += 1
                end_pointer -= 1
            return True