# https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
# 剑指 Offer 17. 打印从1到最大的n位数

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))
