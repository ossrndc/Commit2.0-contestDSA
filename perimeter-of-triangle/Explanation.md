## Approach:

For each test case, we are given `N` sticks with lengths from `1` to `N`.

To determine if a valid non-degenerate triangle can be formed, we check the three largest sticks:
- The three largest sticks are: `N`, `N-1`, and `N-2`.

The triangle inequality theorem states that for any three sides A,B and C (where A< B < C):
    (A+B)>C

Thus, for the sticks `N`, `N-1`, and `N-2`, we need to check if:
- ( (N-2) + (N-1) > N )

Simplifying this:

- ( N > 3 )

So, if (N > 3), the perimeter of the triangle formed by the three largest sticks is (3N - 3).

If (N <= 3), no triangle can be formed, and the result is `-1`.

## Time Complexity:

The time complexity is O(T), where `T` is the number of test cases. For each test case, we perform constant-time operations (a simple comparison and arithmetic).


## Space Complexity:

The space complexity is O(1), since we only use a fixed number of variables, regardless of the input size.


## Constraints:

- 1 ≤ T ≤ 10^4 (up to 10,000 test cases)
- 3 ≤ N ≤ 10^8 (N is at least 3, and can go up to 100 million)
