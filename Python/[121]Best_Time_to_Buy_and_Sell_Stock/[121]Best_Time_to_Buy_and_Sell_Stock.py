# Your Python code goes here.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        max_pro = 0
        while right < len(prices):
            cur_pro = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_pro = max(max_pro, cur_pro)
            else:
                left = right
            right += 1

        return abs(max_pro)
