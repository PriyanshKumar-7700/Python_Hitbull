<<<<<<< HEAD
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
=======
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
>>>>>>> de7137a58bf1772229d0d38a1e6a39ffc98c9906
        return self.fib(n - 1) + self.fib(n - 2)