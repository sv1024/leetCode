//https://leetcode.com/problems/longest-substring-without-repeating-characters/
#include <iostream>

using namespace std;

#include <vector>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> isRepeated(127, -1);
        int maxLenght = 0, cont = 0;
        int i = 0;
        while (i < s.size()) {
            if (isRepeated[s[i]] == -1) {
                cont++;
                isRepeated[s[i]] = i;
                i++;
                if (maxLenght < cont){
                    maxLenght = cont;
                }
            } else {
                s = s.substr(isRepeated[s[i]] + 1);
                isRepeated.assign(127, -1);
                i = 0;
                if (maxLenght < cont){
                    maxLenght = cont;
                }
                cont = 0;
            }
        }
        return maxLenght;
    }
};
