"""
Problem: Solve Me First
Difficulty: Easy
Category: Warmup
URL: https://www.hackerrank.com/challenges/solve-me-first

Description:
Complete the function solveMeFirst to compute the sum of two integers.

Example:
a = 7
b = 3
Return 10
"""

def solve_me_first(a, b):
    return a + b

if __name__ == '__main__':
num1 = int(input())
num2 = int(input())
res = solve_me_first(num1, num2)
print(res)