#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

template<typename T>
void printVector(const std::vector<T>& vec) {
    for (const auto& element : vec) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}

vector<int> reverseArray(vector<int> a) {
    int size = a.size();
    std::cout<<size<<std::endl;
    vector<int> reversed;
    for (int i = size-1; i >= 0; i--)
    {
        reversed.push_back(a[i]);
    }
    return reversed;
}

int main(){
    vector<int> v = {1,2,3};
    vector<int> r = reverseArray(v);
    printVector(r);

}