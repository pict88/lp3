#include <iostream>
#include <string>
using namespace std;

int main() {
    char ch[] = {'a','b','c','d','e','f'};
    int freq[6] = {5,9,12,13,16,45};

    string code[6] = {"","","","","",""};
    string group[6] = {"a","b","c","d","e","f"};

    for(int step = 0; step < 5; step++) {

        int a = -1, b = -1;

        for(int i = 0; i < 6; i++) {
            if(freq[i] == -1) continue;

            if(a == -1 || freq[i] < freq[a]) {
                b = a;
                a = i;
            }
            else if(b == -1 || freq[i] < freq[b]) {
                b = i;
            }
        }

        for(char c : group[a]) {
            for(int i = 0; i < 6; i++) {
                if(ch[i] == c)
                    code[i] = "0" + code[i];
            }
        }

        for(char c : group[b]) {
            for(int i = 0; i < 6; i++) {
                if(ch[i] == c)
                    code[i] = "1" + code[i];
            }
        }

        group[a] += group[b];
        freq[a] += freq[b];
        freq[b] = -1;
        group[b] = "";
    }

    cout << "Huffman Codes:\n";
    for(int i = 0; i < 6; i++) {
        cout << ch[i] << " : " << code[i] << endl;
    }

    return 0;
}
