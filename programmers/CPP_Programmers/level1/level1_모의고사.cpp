#include <string>
#include <vector>
#include <iostream>
#include <algorithm>>

using namespace std;

vector<int> solution(vector<int> answers) {
    
    vector<int> answer;
   
    vector<int> answer1 = { 1, 2, 3, 4, 5 }; 
    vector<int> answer2 = { 2, 1, 2, 3, 2, 4, 2, 5 }; 
    vector<int> answer3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

    vector<int> correct_answer = { 0,0,0 };

    
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == answer1[i%5]) 
            correct_answer[0] += 1;

        if (answers[i] == answer2[i%8]) 
            correct_answer[1] += 1;

        if (answers[i] == answer3[i%10]) 
            correct_answer[2] += 1;
    }
    
    int max_score = *max_element(correct_answer.begin(), correct_answer.end());
   

    for (int i = 0; i < 3; i++) {
        if (correct_answer[i] == max_score) answer.push_back(i + 1);
    }

    return answer;
}

int main() {

    vector<int> input = { 1,2,3,4,5 };

    vector<int> answer;
    
    answer = solution(input);

    for (int i = 0; i < answer.size(); i++) cout << answer[i];
    
    return 0;

    
}

