#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/13 21:33
# @Author: Joy
# @IDE  : PyCharm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = s.__len__() - 1
        index, start, end, max_len = 0, 0, 1, 0
        while index < s_len:
            left, right, count, inner_index = index, s_len, 0, 0
            while left <= right:
                if s[left] == s[right]:
                    count += 1
                    left += 1
                    right -= 1
                else:
                    inner_index += 1
                    left = index
                    right = s_len - inner_index
                    count = 0
            index += 1
            temp_len = left - count - (right + count + 1)
            if temp_len >= max_len:
                start = left - count
                end = right + count + 1
                max_len = temp_len
            if max_len >= s_len - index + 1:
                break
        return s[start:end]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("yoyilli"))
