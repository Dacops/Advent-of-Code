#include <iostream>
#include <vector>
#include <map>

using namespace std;


vector<vector<char>> _inputs;
map<char, int> _values = {
        { 'X', 1 },
        { 'Y', 2 },
        { 'Z', 3 }
};
map<string, int> _wins = {
        { "AX", 3 }, { "BX", 0 }, { "CX", 6 },
        { "AY", 6 }, { "BY", 3 }, { "CY", 0 },
        { "AZ", 0 }, { "BZ", 6 }, { "CZ", 3 }
};

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

int evaluateInput() {

    int score = 0;
    string current;

    for (int i=0; i<(int)_inputs.size()-1; i++) {

        current = "";
        current = current + _inputs[i][0] + _inputs[i][1];
        score += _values[_inputs[i][1]];
        score += _wins[current];
    }

    return score;
}

int main() {
    readInput();
    cout << evaluateInput() << endl;

    return 0;
}