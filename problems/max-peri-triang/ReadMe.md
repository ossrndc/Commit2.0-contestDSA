###                                Max Triangle 
You have N sticks of length 1,2,...,N respectively.

Can you make a non-degenerate triangle with some 3 sticks out of these N sticks? Find the maximum possible perimeter of a triangle you can make, or print −1 if not possible.

  You can make a non-degenerate triangle with sticks of sizes A, B and C if and only if 2*max(A+B+C)<(A+B+C)

   The perimeter of a triangle made with sticks of lengths A,B,C is (A+B+C)


## input format 
The first line of input will contain a single integer T, denoting the number of test cases.

The first and only line of input contains N - the number of sticks.


### Output Format
For each test case, output the maximum perimeter or −1 if not possible.


### constraints

1≤T≤10^4


3≤N≤10^8

**Input** 

    2

    4 
    
    3



**Output**  

   9

   -1


### Explanation
Test Case 1 : You can make a triangle with the sticks of sies 4,3,2. This has the maximum perimeter possible of 4+3+2=9

Test Case 2 : No triangle is possible.