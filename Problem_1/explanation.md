**Explanation**:

**Approach:**

* For every test case, find the number of pages that can be produced from the provided weight of pulp (`N kg`).
* Every kg of pulp produces 1000 pages, so multiply `N` by 1000.
* To calculate the number of notebooks, divide the total number of pages by 100 (as every notebook contains 100 pages).

**Time Complexity**:

* The time complexity is O(1) for each test case since the number of operations per test case is constant (basic arithmetic operations).
* Overall, time complexity is O(T), where T represents the test cases.

**Space Complexity**:

* Space complexity is O(1), since we are using constant space for variables only.