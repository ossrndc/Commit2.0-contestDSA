"""
Problem Statement:
You have N sticks of length 1,2,...,N respectively.
Can you make a non-degenerate triangle with some 3 sticks out of these N sticks?
Find the maximum possible perimeter of a triangle you can make, or print −1 if not possible.
----------------------------------------------------------------------------------------------
input format
The first line of input will contain a single integer T, denoting the number of test cases.
The first and only line of input contains N - the number of sticks.
----------------------------------------------------------------------------------------------
Output Format
For each test case, output the maximum perimeter or −1 if not possible.
----------------------------------------------------------------------------------------------
constraints
1≤T≤10^4
3≤N≤10^8
"""

def max_triangle_perimeter(n : int):
    """
    Calculates the maximum perimeter of a triangle that can be formed using
    N sticks of lengths 1 to `n`.
    The condition for forming a valid triangle is:
        2 * max (A, B, C) < (A + B + C)
    """
    if n <= 3:
        return -1 # no triangle possible
    results = []
    for i in range(n+1):
        # skip the first 3 numbers as they cannot form a triangle
        if i < 3:
            continue
        A = i
        B = i - 1
        C = i - 2
        # check if the triangle can be formed
        if 2 * max(A, B, C) < (A + B + C) :
            results.append(A + B + C)

    return max(results)

if __name__ == "__main__":
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        n = int(input("Enter the number of sticks: "))
        res = max_triangle_perimeter(n)
        if res != -1:
            print(f"Maximum perimeter of triangle: {res}")
        else:
            print(f"{res} : No triangle is possible")

"""
Time Complexity: O(N^2)
Space Complexity: O(1)
----------------------------------------------------------------------------------------------
Sample Input:
Enter the number of test cases: 2
Enter the number of sticks: 5
Enter the number of sticks: 10
----------------------------------------------------------------------------------------------
Sample Output:
Maximum perimeter of triangle: 18
Maximum perimeter of triangle: 27
"""
