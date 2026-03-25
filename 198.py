class Solution:
    def rob(self, nums: List[int]) -> int:
        # 'prev2' represents the max money robbed up to two houses ago
        # 'prev1' represents the max money robbed up to the previous house
        prev1, prev2 = 0, 0
        
        for num in nums:
            # For the current house, we decide:
            # 1. Rob it (num + prev2)
            # 2. Skip it (prev1)
            current = max(prev1, num + prev2)
            
            # Update pointers for the next iteration
            prev2 = prev1
            prev1 = current
            
        return prev1