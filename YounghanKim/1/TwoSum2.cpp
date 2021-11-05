class Solution {
public:
    std::map<int,int> mMap;
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i ++)
        {
            mMap[nums[i]] = i;
        }
        for(int i = 0; i < nums.size(); i ++)
        {
            auto candidate = mMap.find(target - nums[i]);
            if(candidate != mMap.end() && i != candidate->second ) {       
                return vector<int> {i, candidate->second};
            }
        }
        return vector<int> {0, 0};
    }
};
