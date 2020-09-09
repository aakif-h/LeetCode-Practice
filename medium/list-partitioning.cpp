#include "solution.hpp"
using namespace std;


class Solution {
    public:
    vector<string> solve(vector<string>& strs) {
        // Write your code here
        int low,mid,high;
        low = mid = 0;
        high = strs.size()-1;
        
        while (mid <= high) {
            if (!strs[mid].compare("red")) {
                swap(strs[low++], strs[mid++]);
            }
            else if (!strs[mid].compare("blue")) {
                swap(strs[mid],strs[high--]);
            }
            else {
                mid++;
            }
        }
        return strs;
    }
};
