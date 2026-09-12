"""
1143 longest common subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1
Input: text1 = "abcde", text2 = "ace" => You can skip characters
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
"""

# Code (Bottom-Up DP): example got
class Solution:  # pylint: disable=too-few-public-methods
    """Compute the length of the longest common subsequence."""

    def longest_common_subsequence(self, text1, text2):

        """   bottom up
      Base case:
    If either string is empty → LCS length = 0
        """
        if not text1 or not text2:
            return 0

        rows, cols= len(text1) +1, len(text2)+1

        # DP table initialized with 0s.  # dp[i][j] = LCS length of text1[:i] and text2[:j]
        # for _ in range(rows) not i, because the row index isn't needed during initialization. It's the Pythonic style.
        # already know the size of cols and rows above with +1, so no need index like for i in range(rows or cols)
        dp = [[0] * cols for _ in range(rows)] # creates a 2D matrix with rows rows and cols columns.
        # if cols is 4, Python repeats the list 4 times. [0, 0, 0, 0]. if dp =[0 * cols ]=> 0*4, just one 0.
        # This tells readers:I need to loop rows times, but I don't care about the actual index.
        # create initial zeros for both rows and columns to handle empty strings
        # but Why zeros? DP usually starts with base values=0 Represents “no characters matched yet”
        # add +1 to handle base cases (empty string/ zero length)
        # Outer structure: list comprehension: for _ in range(columns + 1) => Each iteration creates one row of the DP table
        # Inner structure: [0] * (rows + 1) => Creates a list of zeros of length rows + 1, where each row is a separate list.”
        # dp[i][j] = length of the LCS between. text1[0..i-1] and text2[0..j-1]
        for i in range(1, rows): # row iterates over numbers from 1 to rows - 1.  # i = row index (text1)
            for j in range(1, cols): # column iterates over numbers from 1 to columns - 1
                if text1[i-1] == text2[j-1]: # If characters match
                    dp[i][j] = 1 + dp[i-1][j-1] # if find a match, 1 + the diagnonal value
                else: # If characters do NOT match
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[rows-1][cols-1]

text1 , text2 = "abcde",  "ace"
obj = Solution()
print(obj.longest_common_subsequence(text1, text2) )# TC: O(column * row), Space: O(m × n)


"""
It simply means:
row iterates over numbers from 1 to columns - 1
column iterates over numbers from 1 to rows - 1

text1[:i] means the substring of text1 from index 0 up to (but not including) index i
text1[0], text1[1], ..., text1[i-1]
So to compute one cell, you need:

Setup
text1 = "abcde" → length m = 5
text2 = "ace" → length n = 3

So dp index would be:
rows = 0 → 5
columns = 0 → 3
row 0 or column 0 = empty string → all zeros

Step 1 Initialize table
               j →
               0   1   2   3
text2          ""  a   c   e
i
0 ""        |  0   0   0   0.       
1 "a"       |  0   1.  1   1
2 "ab"      |  0   1.  1   1
3 "abc"     |  0   1   2   
4 "abcd"    |  0
5 "abcde"   |  0

or 

           ""  a   c   e
        +----------------
""      | 0   0   0   0
a       | 0   .   .   .
ab      | 0   .   .   .
abc     | 0   .   .   .
abcd    | 0   .   .   .
abcde   | 0   .   .   .

Step 2️⃣ Fill the table row by row

Row i = 1 → text1[:1] = "a"
j = 1: "a" == "a" → match
dp[1][1] = dp[0][0] + 1 = 1
j = 2: "a" != "c"
dp[1][2] = max(dp[0][2], dp[1][1]) = 1
j = 3: "a" != "e"
dp[1][3] = 1
0 ""        |  0   0   0   0
1 "a"       |  0   1   1   1

Row i = 2 → "ab"
j = 1: "b" != "a" → max(1,0) = 1
j = 2: "b" != "c" → max(1,1) = 1
j = 3: "b" != "e" → max(1,1) = 1
2 "ab"      |  0   1   1   1

Row i = 3 → "abc"
j = 1: "c" != "a" → 1
j = 2: "c" == "c" → dp[2][1] + 1 = 2
j = 3: "c" != "e" → max(1,2) = 2
3 "abc"     |  0   1   2   2


Row i = 4 → "abcd"
j = 1: "d" != "a" → 1
j = 2: "d" != "c" → 2
j = 3: "d" != "e" → 2
4 "abcd"    |  0   1   2   2

Row i = 5 → "abcde"
j = 1: "e" != "a" → 1
j = 2: "e" != "c" → 2
j = 3: "e" == "e" → dp[4][2] + 1 = 3
5 "abcde"   |  0   1   2   3


Final completed 2D table
           ""  a   c   e
        +----------------
""      | 0   0   0   0
a       | 0   1   1   1
ab      | 0   1   1   1
abc     | 0   1   2   2
abcd    | 0   1   2   2
abcde   | 0   1   2   3


Step 3️⃣ Answer
dp[5][3] = 3
So:
LCS length = 3
LCS = "ace"

dp[i-1][j-1] (diagonal)
dp[i-1][j] (up)
dp[i][j-1] (left)

dp[i][j] = LCS length of text1[:i] and text2[:j]


Rows = i = 0 → m
Columns = j = 0 → n

dp[0][*] = 0 (empty prefix of text1)
dp[*][0] = 0 (empty prefix of text2)



"""

# Space Optimized DP (Only 2 rows)
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    prev = [0]*(n+1)
    curr = [0]*(n+1)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, [0]*(n+1)  # move to next row

    return prev[n]
# Time: O(m*n)



"""

Label the Grid. Empty string base case
        ""   a   c   e
      ----------------
""    | 0 | 0 | 0 | 0 |
a     | 0 |   |   |   |
b     | 0 |   |   |   |
c     | 0 |   |   |   |
d     | 0 |   |   |   |
e     | 0 |   |   |   |

then match rule follows, if there's a match 1 + diagnonal row-1 and column-1
Why +1?
We need an extra row and column to represent the empty string case.
dp[0][*] → comparing empty text1 with text2
dp[*][0] → comparing text1 with empty text2
Example for text1 = "abc", text2 = "ac":
[[0] * (rows + 1) for _ in range(columns + 1)] This creates a 2D list (matrix).
dp = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
4 rows (len(text1)+1)
3 columns (len(text2)+1)

Loops columns + 1 times
_ means: “I don’t care about the loop variable”
Each loop creates one new row

"""


# https://www.youtube.com/watch?v=NswCa9VKGXY code source
class SolutionVideo:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        dp = [[0 for i in range(cols)] for j in range(rows)] # initizalze zero for both rows and columns
        for row in range(1, rows): # loop through two dimensional
            for col in range(1, cols):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[row][col]