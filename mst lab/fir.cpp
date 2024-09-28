#include <bits/stdc++.h>
using namespace std;
int main() {
    string input = "XYX";
    int count = 0;
    for(int i = 1; i < input.size(); i++) {
        if(input[i - 1] == input[i]) count++;
    }
    cout << count;
    return 0;
}