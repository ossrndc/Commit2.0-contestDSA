# Explanation

## Problem Overview

You are given `N` sticks of lengths 1 through N. You need to determine whether it is possible to form a **non-degenerate triangle** using any three sticks. If it is possible, you must return the **maximum perimeter** that can be formed. Otherwise, return `-1`.

### Non-degenerate Triangle Condition:
A triangle with sides A, B, and C is non-degenerate if:
```

A + B > C
B + C > A
C + A > B

```

## Approach

To get the **maximum perimeter**, we should try using the three **longest sticks**, which are:
```

N, N-1, N-2

```

We check if these three can form a valid triangle:
- The largest side is `N`.
- The sum of the other two sides is `N-1 + N-2`.

So the condition becomes:
```

(N-1 + N-2) > N

```

Simplifying:
```

2N - 3 > N
\=> N > 3

```

### Final Logic:
- If `N > 3`, then sticks `N`, `N-1`, `N-2` can form a triangle.
  - The maximum perimeter is `N + (N-1) + (N-2) = 3N - 3`.
- If `N <= 3`, output `-1` (triangle not possible with smallest lengths).

## Time and Space Complexity

- **Time Complexity:** O(1) per test case → Overall O(T)
- **Space Complexity:** O(1)

## Sample Walkthrough

### Input:
```

2
4
3

```

### Output:
```

9
-1

```

- For `N = 4`: Use sticks 4, 3, 2 → valid triangle → perimeter = 9
- For `N = 3`: Use sticks 3, 2, 1 → not a valid triangle → output = -1
```

