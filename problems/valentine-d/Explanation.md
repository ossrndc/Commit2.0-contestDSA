<!-- Approach:

Input Handling:

Read the number of test cases T.

For each test case, read X (total money) and Y (cost per chocolate).

Calculation:

If Y = 0, output 0 (though constraints ensure Y ≥ 1, we handle it for safety).

Otherwise, compute X // Y (integer division) to get the maximum number of chocolates.

Output:

Print the result for each test case.

Time Complexity:

O(T), where T is the number of test cases.

Each test case is processed in constant time O(1).

Space Complexity:

O(1), as no extra space is used beyond input variables. -->