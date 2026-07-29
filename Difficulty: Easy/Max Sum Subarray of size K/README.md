# [Max Sum Subarray of size K](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/0)
Difficulty Level : Difficulty: Easy

Given an array of integers
 arr[] 
 and a number
 k
. Return the maximum sum of a subarray of size k.


Note:
 A subarray is a contiguous part of any given array.


Examples:


Input:
 arr[] = [100, 200, 300, 400], k = 2

Output: 
700

Explanation: 
arr
2
 
+ arr
3
 = 700, which is maximum.


Input: 
arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4

Output: 
39

Explanation: 
arr
1
 + arr
2
 + arr
3 
+ arr
4
 = 39, 
which is maximum.


Input:
 arr[] = [100, 200, 300, 400], k = 1

Output: 
400

Explanation: 
arr
3
 = 400, which is maximum.


Constraints:
1 ≤ arr.size() ≤ 10
6
0 ≤ arr[i] ≤ 10
6
1 ≤ k ≤ arr.size()

Company Tags :OYO Rooms NPCI
Topic Tags :prefix-sum sliding-window Misc
