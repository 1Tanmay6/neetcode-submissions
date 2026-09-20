class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # n = len(s)
        # m = len(t)
        # value_dict: dict[str, int] = {}
        # if n != m:
        #     return False
        # else:
        #     for i in range(n):
        #         keys = value_dict.keys()
        #         char_s = s[i]
        #         char_t = t[i]

        #         if char_s in keys:
        #             value_dict[char_s] += 1
        #         else:
        #             value_dict[char_s] = 1
                
        #         if char_t in keys:
        #             value_dict[char_t] -= 1
        #         else:
        #             value_dict[char_t] = -1
        # set_of_values = set(value_dict.values())
        # return 0 in set_of_values and not len(set_of_values) > 1

        return sorted(s) == sorted(t)