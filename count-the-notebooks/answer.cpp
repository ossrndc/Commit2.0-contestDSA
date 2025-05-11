
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T; // Number of test cases

    while (T--) {
        int N;
        cin >> N; // Weight of the pulp in kgs

        // 1 kg of pulp can make 1000 pages, and each notebook consists of 100 pages.
        int notebooks = (N * 1000) / 100;

        cout << notebooks << endl;
    }

    return 0;
}