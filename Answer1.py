#Problem Statement: You know that 1 kg of pulp can be used to make 1000 pages and 1 notebook consists of 100 pages.

"""
Input Format :
First line will contain T, the number of test cases. Then the test cases follow.
Each test case contains a single integer N - the weight of the pulp the factory has (in kgs).
------------------------------------------------------------------------------------------------
Output Format
For each test case, output the number of notebooks that can be made using N kgs of pulp.
-------------------------------------------------------------------------------------------------
Constraints
1≤T≤100
1≤N≤100
"""

# Solution
def count_notebook(n: int):
    """
    This function takes the weight of pulp in kilograms, calculates the total number of
    pages that can be created from the pulp, and determines the number of 100-page
    notebooks that can then be made.
    """
    # no of Pages in n kg pulp
    pages = n * 1000
    # no of notebooks required
    nb = pages // 100
    return nb

if __name__ == "__main__":
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        n = int(input("Enter the weight of pulp in kilograms: "))
        print(f"Number of notebooks required: {count_notebook(n)}")

"""
Time Complexity: O(1)
Space Complexity: O(1)
----------------------------------------------------------------------------------------------
Sample Input:
Enter the number of test cases: 2
Enter the weight of pulp in kilograms: 10
Enter the weight of pulp in kilograms: 20
----------------------------------------------------------------------------------------------
Sample Output:
Number of notebooks required: 100
Number of notebooks required: 200
"""