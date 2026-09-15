class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> heap;
        unordered_map<int, int> map;

        for(int i: nums){
            map[i]++;
        }

        for(auto it: map){
            heap.push({it.second, it.first});
        }

        vector<int> ans;

        for(int i=0; i<k; i++){
            ans.push_back(heap.top().second);
            heap.pop();
        }

        return ans;
    }
};
