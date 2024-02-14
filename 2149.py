class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        pos = 0
        neg = 1
        for i in nums:
            if i>0:
                ret[pos] = i
                pos+=2
            elif i<0:
                ret[neg] = i
                neg +=2
        return ret
