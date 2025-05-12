# Explanation

## Problem Overview

Ayushman wants to buy chocolates on Valentine's Day. For each test case, we are given:

- `X`: The total money Ayushman has.
- `Y`: The cost of one chocolate.

We need to calculate how many full chocolates he can buy.

## Approach

To find the maximum number of chocolates Ayushman can buy, we use **integer division**:

```

number\_of\_chocolates = X // Y

```

This ensures only whole chocolates are counted (since he can't buy half a chocolate).

### Steps:
1. Read the number of test cases `T`.
2. For each test case:
   - Read two integers `X` and `Y`.
   - Compute the result using `X // Y`.
   - Print the result.

## Sample Walkthrough

### Sample Input
```

4
5 10
16 5
35 7
100 1

```

### Sample Output
```

0
3
5
100

```

- `5 // 10 = 0` → Not enough money.
- `16 // 5 = 3` → Can buy 3 chocolates.
- `35 // 7 = 5` → Exact fit for 5 chocolates.
- `100 // 1 = 100` → Each chocolate costs 1 rupee.

## Time and Space Complexity

- **Time Complexity**: O(T), where T is the number of test cases.
- **Space Complexity**: O(1), as only a few variables are used.

## Notes

- This solution uses simple arithmetic and is efficient within the given constraints (`1 ≤ T, X, Y ≤ 100`).
- Python’s `//` operator handles integer division cleanly and avoids floating-point issues.
