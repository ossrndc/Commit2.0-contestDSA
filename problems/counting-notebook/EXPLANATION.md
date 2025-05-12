<!-- Approach:

Input Handling:

Reading.. the number of test cases T.

For each test case, read the weight of pulp N (in kg).

Calculation:

Pages Calculation: Since 1 kg = 1000 pages, N kg = N * 1000 pages.

Notebooks Calculation: Each notebook requires 100 pages, so the number of notebooks = (N * 1000) / 100 = N * 10.

Output:

Print the result for each test case.

Time Complexity:

O(T), where T is the number of test cases.

Each test case is processed in constant time as the loop for single time for each individual case O(1).

Space Complexity:
Memory is well maintained just taking input
O(1), as no extra space is used beyond input variables. -->