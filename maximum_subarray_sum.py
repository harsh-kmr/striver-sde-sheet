#https://www.naukri.com/code360/problems/maximum-subarray-sum_630526

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    max_sum_so_far = max_sum_till_now  = 0
    for i in range(n):
        max_sum_so_far += arr[i]
        if max_sum_till_now < max_sum_so_far:
            max_sum_till_now = max_sum_so_far
        elif max_sum_so_far <0 :
            max_sum_so_far = 0
    
    return max_sum_till_now
