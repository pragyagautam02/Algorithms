class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.solve(0,nums,[])
        return self.result
    def solve(self, i , nums , out):
        if i == len(nums):
            self.result.append(out)
            return
        out1 = copy.deepcopy(out)
        out2 = copy.deepcopy(out)
        out1.append(nums[i])
        self.solve(i+1 , nums , out1)
        self.solve(i+1 , nums , out2)