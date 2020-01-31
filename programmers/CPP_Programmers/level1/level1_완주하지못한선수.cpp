#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    bool IsErase = false;

    string answer = "";

    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    for (int i = 0; i < participant.size(); i++) {
       if( participant[i] != completion[i]) return participant[i];
    }
}

int main() {
    
    vector<string> input = { "leo" , "kiki " , "eden" };

    vector<string> input2 = { "kiki" , "eden" };

    solution(input, input2);
    
    return 0;

}