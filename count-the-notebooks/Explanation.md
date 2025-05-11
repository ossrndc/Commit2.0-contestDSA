## Approach:

For each test case, we are given n kilograms of pulp.

Since 1 kg of pulp can produce 1000 pages, and each notebook consists of 100 pages, the number of notebooks we can create is simply:

notebooks = (N*1000)/100 or N*10

## Time Complexity:

The time complexity is o(T)
T is the number of test cases. For each test case, we perform constant-time arithmetic operations.

## Space Complexity:

The space complexity is O(1)
O(1) if we ignore the input/output storage, as we're only storing a few integers at any point in time.


## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 100