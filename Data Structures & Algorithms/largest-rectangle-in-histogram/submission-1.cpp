class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int count=1, maxi=0;
        int area = 0;
        auto max_it = max_element(heights.begin(), heights.end());
        if (max_it != heights.end()) maxi = *max_it;
        while(count <= maxi){
            int i=0, j=0;
            while(j < heights.size() && i <= j){
                if(heights[j] >= count){
                    j++;
                }
                else{
                    int temp = count * (j - i);
                    area = max(area, temp);
                    i = j+1;
                    j++;
                }
            }
            int temp = count * (j - i);
            area = max(area, temp);
            count++;
        }
        return area;
    }
};
