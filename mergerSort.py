#!/bin/bash/python
'''
https://oj.leetcode.com/problemset/algorithms/#88
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
'''
class Solution:
	def merge(self, A, m, B, n):
		i = m - 1
		j = n - 1
		k = m + n - 1
		# compare from the biggest of list A and B to choose the bigger one in order to set to the position k
		while i >= 0 and j >= 0:
			if A[i] > B[j]:
				A[k] = A[i]
				i-=1
				k-=1
			else:
				A[k] = B[j]
				j-=1
				k-=1

		while j >= 0:
			A[k] = B[j]
			j-=1
			k-=1

	def merge2(self, A, m, B, n):
		if m == 0:
			for i in range(0, n):
				A.append(B[i])
		elif n == 0:
			pass
		elif B[0] > A[m-1]:
			A.extend(B)
		else:		 
			temp = 0  # save the temp value for B[i] to compare with A[j]
			k = 0     # save the index of A[k] to move A item to right
			higher = m-1 # track the size of A 
			lower = 0

			for i in range(0, n):
				for j in range(lower, higher+1)[::-1]: # loop from back to front
					if (B[i] < A[j]): 
						temp = B[i]
						k = j
						A.append(A[k]);
						# find the appropriate position for the B[i]
						while k > 0 and temp < A[k-1]:
							A[k] = A[k-1]
							k-=1
					
						A[k] = temp
						higher = m + i
						lower = k
						break
					else: # append the B[i] to A, and increase the size of higher
						A.append(B[i])
						higher = m + i
						lower = j + 1
						break	

solution = Solution();
#print solution.merge([12,32,42,52,59],5,[1,2,15,35,123],5);
#a = [2, 5, 6, 9, 12]
#b = [1, 3, 5, 7, 10]
a = []
b = []
solution.merge2(a,len(a),b,len(b));
