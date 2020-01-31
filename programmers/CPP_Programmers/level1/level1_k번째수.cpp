#include <iostream>
#include <string>
#include <algorithm>>
#include <vector>


using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
   

    vector<int> answer;
     
   
    for(int i = 0; i < commands.size(); i++){
        vector<int> temp;
        
        int start = commands[i][0];
        int end = commands[i][1];
        int v_index = commands[i][2];

        if (start == end) answer.push_back(array[start-1]);

        else {
            for (int j = start - 1; j <= end - 1; j++) {
                temp.push_back(array[j]);
            }            
            sort(temp.begin(), temp.end());         
            answer.push_back(temp[v_index-1]);
        }
   
    }


    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i];
   }

    return answer;
}
