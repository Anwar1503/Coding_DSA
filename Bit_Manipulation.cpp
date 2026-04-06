// https://leetcode.com/problems/single-number/submissions/1970804526/

#include<iostream>
using namespace std;
#include <vector>

int FindSingle(const std::vector<int> &nums)
{
    int result = 0;
    for (int num : nums)
    {
        result ^= num;
    } 
    return result;
}

int main()
{
    std::vector<int> arr = {2,2,1};
    int result = FindSingle(arr);
    std::cout<<"result :"<<result;
}