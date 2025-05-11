"""
Problem Statement:
Valentine's Day is approaching and thus Ayushman wants to buy some chocolates for someone special.
Ayushman has a total of X rupees and one chocolate costs Y rupees.
What is the maximum number of chocolates Ayushman can buy?
----------------------------------------------------------------------------------------------------
Input Format
First line will contain T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, two integers X,Y -
the amount Ayushman has andthe cost of one chocolate respectively.
----------------------------------------------------------------------------------------------------
Output Format
For each test case, output the maximum number of chocolates Ayushman can buy.
----------------------------------------------------------------------------------------------------
Constraints
1≤T≤100
1≤X,Y≤100
"""

#Solution
def chocolates_count(rup:int,cost:int):
    """
    Calculates the number of chocolates that can be purchased with the given
    amount of money and the cost of a single chocolate.
    """
    return rup//cost

if __name__ == "__main__":
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        rup,cost = map(int,input("Enter the amount of money and cost of a single chocolate: ").split())
        print(f"Number of chocolates purchased: {chocolates_count(rup,cost)}")

"""
Time Complexity: O(1)
Space Complexity: O(1)
----------------------------------------------------------------------------------------------
Sample Input:
Enter the number of test cases: 2
Enter the amount of money and cost of a single chocolate: 10 2
Enter the amount of money and cost of a single chocolate: 15 3
----------------------------------------------------------------------------------------------
Sample Output:
Number of chocolates purchased: 5
Number of chocolates purchased: 4
"""