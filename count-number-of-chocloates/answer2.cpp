#include <iostream>
using namespace std;

int main() {
    int T;  // Number of test cases
    cin >> T;
    
    while(T--) {
        int X, Y;
        cin >> X >> Y;  // Reading X (the amount Ayushman has) and Y (cost of one chocolate)
        
        // Calculating the maximum number of chocolates Ayushman can buy
        int maxChocolates = X / Y;
        
        // Result
        cout << maxChocolates << endl;
    }
    
    return 0;
}
