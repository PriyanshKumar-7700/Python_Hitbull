<<<<<<< HEAD
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}

        def helpFunction(n):
            if n <= 2:
                return n
            if n in d:
                return n
            temp = helpFunction(n-1) + helpFunction(n-2)
            d[n] = temp
            return temp
        
=======
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}

        def helpFunction(n):
            if n <= 2:
                return n
            if n in d:
                return n
            temp = helpFunction(n-1) + helpFunction(n-2)
            d[n] = temp
            return temp
        
>>>>>>> de7137a58bf1772229d0d38a1e6a39ffc98c9906
        return helpFunction(n)