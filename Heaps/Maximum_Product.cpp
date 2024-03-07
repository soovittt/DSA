#include <iostream>
#include <vector>
#include <queue>
using namespace std;



template <typename T>
void printPriorityQueue(priority_queue<T> pq) {
    while (!pq.empty()) {
        cout << pq.top() << " ";
        pq.pop();
    }
    cout << endl;
}


int maxProduct(vector<int> &nums) {
    priority_queue<int> heap;
    for (unsigned int i = 0; i < nums.size(); i++)
    {
        heap.push(nums[i]);
    }

    int firstMax = heap.top();
    heap.pop();
    int secondMax = heap.top();
    heap.pop();
    return (firstMax-1)*(secondMax-1);
    
}

int main() {
  vector<int> myVector = {1,5,4,5};
  cout<<maxProduct(myVector);
  return 0;
}