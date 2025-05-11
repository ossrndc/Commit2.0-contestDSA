## Approach:

For each test case, we are given `X` rupees (the amount Ayushman has) and `Y` rupees (the cost of one chocolate).

To calculate how many chocolates Ayushman can buy, we can simply divide the total money `X` by the cost of one chocolate `Y`. 

The result is:      maxChocolates = X / Y (integer)

which gives us the maximum number of chocolates Ayushman can afford.

## Time Complexity:

The time complexity is O(T), where `T` is the number of test cases. For each test case, we perform constant-time arithmetic operations (integer division).

## Space Complexity:

The space complexity is O(T). We are only storing a few integer variables (like `X`, `Y`, and `max_chocolates`), so the space used is constant.

## Constraints:

- 1 ≤ T ≤ 100 
- 1 ≤ X, Y ≤ 100 
