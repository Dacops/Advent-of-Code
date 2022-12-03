#include <iostream>
#include <vector>
#include <map>

using namespace std;


vector<vector<char>> _inputs;

void readInput() {

    int i = 0;
    _inputs.resize(1);
    _inputs[i].resize(2*sizeof(char));

    while (cin>>_inputs[i][0], cin.ignore(), cin>>_inputs[i][1]) {
        i++;
        _inputs.resize(i+1);
        _inputs[i].resize(2*sizeof(char));
    }
}

void changeInput() {

    vector <char> outcomes = {'X','Y','Z'};

    for (int i=0; i<(int)_inputs.size()-1; i++) {
        switch(_inputs[i][1]) {
            case('X'): { _inputs[i][1] = outcomes[(_inputs[i][0]-('A'-2))%3]; break;}
            case('Y'): { _inputs[i][1] = outcomes[_inputs[i][0]-'A']; break; }
            case('Z'): { _inputs[i][1] = outcomes[(_inputs[i][0]-('A'-1))%3]; break; }
        }
    }
}

int evaluateInput() {

    int score = 0;
    vector<int> vals = {3,6,0};

    for (int i=0; i<(int)_inputs.size()-1; i++) {
        score+=( (int(_inputs[i][1])-('X'-1)) +
                 vals[ (3 + (int(_inputs[i][1])-'X') - (int(_inputs[i][0])-'A')) % 3 ]);
    }
    return score;
}

int main() {
    readInput();
    changeInput();
    cout << evaluateInput() << endl;

    return 0;
}