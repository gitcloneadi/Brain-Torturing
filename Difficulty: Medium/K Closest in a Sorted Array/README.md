Find k closest elements

Difficulty: Medium
Accuracy: 15.96%
Submissions: 99K+
Points: 4
Average Time: 30m

Given a sorted array arr[] of unique integers, an integer k, and a target value x. Return exactly k elements from the array closest to x, excluding x if it exists.

An element a is considered closer to x than b if:

· |a - x| < |b - x|, or
· |a - x| == |b - x| and a > b (prefer the larger element in case of a tie)

Return the k closest elements in order of closeness (closest first).

---

Examples:

Example 1:

Input:
arr[] = [1, 3, 4, 10, 12], k = 2, x = 4
Output: [3, 1]

Explanation:

· 4 is excluded from consideration.
· Closest element to 4 is 3 (distance 1).
· Next closest is 1 (distance 3).

---

Example 2:

Input:
arr[] = [10, 20, 30, 40, 50], k = 3, x = 25
Output: [30, 20, 40]

Explanation:

· First closest → 30 (distance 5, and 30 > 20 so preferred over 20).
· Second closest → 20 (distance 5).
· Third closest → 40 (distance 15).

---

Constraints:

· 1 ≤ arr.size() ≤ 10⁵
· 1 ≤ arr[i] ≤ 10⁶
· 1 ≤ k ≤ arr.size()
· 1 ≤ x ≤ 10⁶

---

Expected Complexities:

· Time Complexity: O(log n + k)
· Space Complexity: O(k)

---

Company Tags:

· Amazon
· OYO Rooms

Topic Tags:

· Arrays
· Binary Search
· Two Pointers
· Sorting

Related Articles:

· Find K Closest Elements (LeetCode)
