#include <iostream>
using namespace std;

int main() {
   
    int T;
    cin >> T;  // The number of test cases
    
    while(T--){
        
        int N;
        cin >> N; // Read the value of N for the current test case
        
        if (N < 3) {
            cout << -1 << endl; // If N is less than 3, we cannot form a triangle
            
        } 
        else {
            // Check the triangle inequality for the three largest sticks: N, N-1, and N-2
            if ((N-2) + (N-1) > N) {
                cout << 3*N - 3 << endl;    // Otherwise, calculate the maximum perimeter: 3 * N - 3
            } 
            
            else {
                cout << -1 << endl; // If the triangle inequality is not satisfied, print -1
            }
    }
}
    return 0;
}
