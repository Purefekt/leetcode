class NumArray:

    def __init__(self, nums: List[int]):
        self.psum = [0]
        cur = 0
        for n in nums:
            cur += n
            self.psum.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right+1] - self.psum[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)