<!-- Approach:

Input Handling:

Reading  the number of test cases T

T.

For each test case, reading N

N, the number of sticks.

Triangle Validity Check:

For 
N<=3
N≤3, it's impossible to form a valid triangle (output -1).as per certified rule of triangle it is necessary thatsome of any two side should be greater than 3rd side

For 
N>3
N>3, the maximum perimeter is 

3N−3, derived(N+N-1+N-2) largest sticks 

N,N−1,N−2, which always satisfy the triangle inequality 
2*max(A+B+C)<(A+B+C)

Output:

Print the result for each test case.

Time Complexity:

O(T), where 

T is the number of test cases.

Each test case is processed in constant time 

O(1).

Space Complexity:

O(1), as no extra space is used beyond input variables. -->