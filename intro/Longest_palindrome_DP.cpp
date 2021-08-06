#include <iostream>
#include <string>
using namespace std; 

// DP solution
class Solution {
public:
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    string longestPalindrome(string &s) {
        int len = s.length();
        vector<vector<int>> isPalindrome(len, vector<int>(len));
        int maxLen = 1;
        int start = 0;
        
        for (int i = 0; i < len; i++) {
            isPalindrome[i][i] = 1;
        }
        for (int i = 0; i + 1 < len; i++) {
            if (s[i] == s[i + 1]) {
                isPalindrome[i][i + 1] = 1;
                maxLen = 2;
                start = i;
            }
        }
        for (int left = len - 1; left >= 0; left--) {
            for (int right = left + 2; right < len; right++) {
                if (isPalindrome[left + 1][right - 1] == 1
                        and s[left] == s[right]) {
                    
                    isPalindrome[left][right] = 1;
 
                    if (right - left + 1 > maxLen) {
                        maxLen = right - left + 1;
                        start = left;
                    }
                }
            }
        }
        return s.substr(start, maxLen);
    }
};

int main(){
    Solution sol;
    string s="acca"; 
    cout<< " Checkign string "<<s<<  " is palindrome? "<< sol.longestPalindrome(s); 

}