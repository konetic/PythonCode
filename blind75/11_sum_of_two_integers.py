"""
371. Sum of Two Integers
"""


# Classic Bit Manipulation (XOR + AND + SHIFT)

class Solution:
    def get_sum(self, a: int, b: int) -> int:
        while b: #  while b!=0: Continue looping as long as b is not 0. b stores the carry. Once there 
            # are no carries left (b == 0), the result is complete

            # a = a ^ b  if we do this first, it returns early
            carry= (a & b) << 1 # find a & b then shift that value by 1 a^ b is exclusive or
            a= a ^ b # # Step 2: stor the xor in a and continue to carry.  # Add without carry i.e (XOR adds bits but throws away any carry)
            b = carry # Step 3: store the carry in b and continue
            # adding carry until the carry becomes zero
        return a # if we don't have a carry, i.e we're done and just return a. The result is stored in a, and b is 0, 
            # so we can return a as the final sum.

obj = Solution()
print(obj.get_sum(9,11)) # 20



"""
371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.
Example 1:
Input: a = 1, b = 2
Output: 3

# Method 1: Iterative Without Mask (Conceptual / Language-Neutral)

Why It Works

XOR = sum

AND + shift = carry

Loop until carry disappears

⛔ Python issue: negative numbers break without mask
🟡 Mention in interviews, but clarify Python limitation



# Method 5: Math Tricks (NOT Allowed)
sum = a - (-b)



# Using Lambda + Loop (modern Python)
getSum = lambda a, b: a if b == 0 else getSum(a ^ b, (a & b) << 1)
print(getSum(3, 4))


"""
Key Idea: a^b and a&b are the equivalence of addition.
Operation	Meaning
a ^ b	Add bits without carry
a & b	Find carry bits
<< 1	Shift carry to correct position

Example: a=9, b=211
a= 9 = 1001
b= 11= 1011 
a^b =  0010. this sum gives integer 2. But we know that 9+11 is 20. So need to do the carry. Now the arries are at 
        the very  begining and 1 at last. get the carry , shift to the left and add to the xor value; 0010

like 1001
a= 9 = 1001
b= 11= 1011  when we add using xor, we got 0010 and what's left is the carry
a&b<<1= 1001 this value got by adding the above carries.

now add both 0010 and 1001. a&b needs to shift to the left by 1 first. so add 0 the rightmost end and would be 
10010. and add 0 to the left most to xor. so that it would be 00010
     00010
     10010
then do xor and a&b operation again until a&b is zero. So add both, apply the above methods again
         00010
         10010  
a^b =    10000 of the above xor addition
a&b =    00100

       again do xor operation
a^b =    10000 
         00100   gives    10100 this is a ^ b
a& b     00000  do a&b operation again. if a&b is zeros, that means we don't have a carry. i.e we are done.
        no carry, i.e & operation is zeros and the solution would be the xor operation result which is 10100


⏱ Time: O(1) constant time
📦 Space: O(1)
🟢 Best interview answer
"""


"""
# 1) Recursive Bitwise Solution
def getSum(a, b):
    if b == 0: # b= carry
        return a   # Base case: if no carry → return a
    return getSum(a ^ b, (a & b) << 1) # a ^ b → sum without carry, (a & b) << 1 → as carry.
    # addition using bitwise operations. ^ → is the bitwise XOR (exclusive OR) operator
    # a ^ b => a XOR b. Exclusive OR. XOR rule (per bit) if either a or be has 1, the value(addition) would be 1
    # conversely, if both values are 1, return 0, any carry 1.
    # The recursion should continue until the carry is zero, because once carry is zero, there’s nothing left to add.
print(getSum(3, 4)) # TC Time Complexity: O(1), it is O(k) where k = number of bits.
example
XOR rule (per bit):
XOR is (definition): XOR = “exclusive OR”
For each bit position:
    1) If the two bits are different i.1 1, and 0 → result is 1
    2) If the two bits are the same → result is 0
<< → left shift operator
<< 1 → shift bits one position to the left
Why shift?
Carry moves to the next higher bit in addition.
"""