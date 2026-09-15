class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        for(string it: strs){
            string s = it;
            sort(it.begin(), it.end());

            map[it].push_back(s);
            
        }

        vector<vector<string>> ans;

        for(auto it: map){
            ans.push_back(it.second);
        }

        return ans;
    }
};
