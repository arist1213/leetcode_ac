#/bin/bash/python
'''
https://oj.leetcode.com/problemset/algorithms/#70
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
'''
class Solution:
	def climbStairs(self, n):			
		if n == 0:
			return n
		else:
			k = n/2
			ways = 0
	
			for i in range(0, k+1):
				print "m=%d,n=%d" %(i, n - i*2)
				ways += self.f(i, n - i*2)	
				print "ways=%d" %(ways)

			return ways
	
	def f(self, m, n):
		if m == 0 or n == 0:
			return 1
		else:
			#return self.f(m-1, n)+self.f(m, n-1)
			return self.f(m-1, n)*(n+m)/m	

solution = Solution()
print solution.climbStairs(35)
