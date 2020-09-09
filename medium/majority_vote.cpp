#include "solution.hpp"
using namespace std;


class Solution {
    public:
    int solve(vector<int>& nums) {
        // Write your code here
        int candidate, count, n;
        candidate = count = 0;
        n = nums.size();
        for (int i = 0; i < n; i++) {
            if (!count) {
                candidate = nums[i];
            }
            count += candidate == nums[i] ? 1 : -1;
        }
        count = 0;
        for (int i = 0; i < n; i++) {
            if (candidate == nums[i]) {
                count++;
            }
        }
        return count > n/2 ? candidate : -1;
    }
};
