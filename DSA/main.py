
def add_numbers(a, b):
    return a + b

# sorting.py

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def unique_paths(m,n):
    """
    url: https://leetcode.com/problems/unique-paths/description/
    - Based on an m x n grid, calculate number of unique paths to travel from top left to bottom right.
    """
    ##### Dp method (inefficient)
    # dp = [[0 for _ in range(n)] for _ in range(m)]
    # for i in range(m):
    #     for j in range(n):
    #         if i == 0 and j == 0:
    #             dp[i][j] = 1
    #         elif i == 0:
    #             # take into account of top grid
    #             dp[i][j] = dp[i][j - 1]
    #         elif j == 0:
    #             # take into account of left grid
    #             dp[i][j] = dp[i - 1][j]
    #         else:
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # return dp[-1][-1]

    ##### Combination
    from math import comb
    no_of_down, no_of_right = m-1, n-1  # starting is at idx (0,0)
    return comb(no_of_down + no_of_right, no_of_right)  # combination of total steps while choosing right/down: n!/(r! * (n-r)!)

def uniquePathsWithObstacles(obstacleGrid):
    """
    url: https://leetcode.com/problems/unique-paths-ii/
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    if obstacleGrid[0][0] == 0:
        dp[0][0] = 1

    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]

    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0: 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


def minPathSum(grid):
    """
    url: https://leetcode.com/problems/minimum-path-sum/
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])

    dp = [ [0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i-1]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]

def largestContiguousSum(arr: list[int]) -> int:
    """
    https://workat.tech/problem-solving/practice/largest-contiguous
    """
    # add your logic here
    import math
    cummulative = arr[0]
    stage = 0
    max_result = -math.inf
    for i in range(1, len(arr)):
        if cummulative < 0:
            cummulative = arr[i]
        elif arr[i] >= 0 and cummulative + stage >= 0:
            cummulative += arr[i] + stage
            stage = 0
        elif arr[i] >= 0 and cummulative + stage < 0:
            max_result = cummulative
            cummulative = arr[i]
            stage = 0
        else:
            stage += arr[i]
    return max(max_result, cummulative)

def allsorted():
    """
    https://visualgo.net/en/sorting
    """
    return 

class Solution(object):
    def trap(self, height):
        """
        url: https://leetcode.com/problems/trapping-rain-water/?envType=company&envId=goldman-sachs&favoriteSlug=goldman-sachs-thirty-days
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        
        left_arr = [0] * n
        right_arr = [0] * n
        left_arr[0] = height[0]
        right_arr[-1] = height[-1]

        for i in range(1, n):
            left_arr[i] = max(left_arr[i-1], height[i])
        for i in range(n-2, -1,-1):
            right_arr[i] = max(right_arr[i+1], height[i])
        
        water = 0
        for i in range(n):
            water += min(left_arr[i], right_arr[i]) - height[i]
        return water

from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        url: https://leetcode.com/problems/valid-parentheses/
        :type s: str
        :rtype: bool
        """
        stack = deque()
        mapping = {"(":")", "{": "}", "[":"]"}

        for i in s:
            if i in mapping:
                stack.append(mapping[i])
                continue
            if len(stack) != 0 and stack.pop() == i:
                continue
            else:
                return False
        return len(stack) == 0

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        substring = ""
        max_length = 0
        for i in s:
            idx = substring.find(i)
            substring += i
            if idx != -1:
                if max_length < len(substring) - 1:
                    max_length = len(substring) - 1
                substring = substring[idx+1:] 

        if max_length < len(substring):
            max_length = len(substring)
        return max_length

class Solution(object):
    def merge(self, intervals):
        """
        url: https://leetcode.com/problems/merge-intervals/
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1] = [result[-1][0], max(intervals[i][1], result[-1][1]) ]
            else:
                result.append(intervals[i])
        return result
        


# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/6723070/video-divide-each-array-into-two-groups/
if __name__ == "__main__":
    from math import comb
    # print(comb(8,6))

    print(largestContiguousSum([1,2,3,4,5]))
    print(largestContiguousSum([4,-6,2,5]))
    print(largestContiguousSum([1,-2,3,4,-5]))
    print(largestContiguousSum([6,-4,2,5]))
    print(largestContiguousSum([-6,-4,2,5]))
    print(largestContiguousSum([4,-6,-2,5]))
    pass