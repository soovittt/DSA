#include <iostream>
#include <vector>

using namespace std;



template <typename T>
void printVector(const vector<T>& vec) {
    cout << "[ ";
    for (const T& element : vec) {
        cout << element << " ";
    }
    cout << "]" << endl;
}

void heapifySubtree(vector<int>& arr, int n, int i) {
    int smallest = i;
    int leftChild = 2 * i + 1;
    int rightChild = 2 * i + 2;

    // Check if the left child exists and is smaller than the current smallest
    if (leftChild < n && arr[leftChild] < arr[smallest]) {
        smallest = leftChild;
    }

    // Check if the right child exists and is smaller than the current smallest
    if (rightChild < n && arr[rightChild] < arr[smallest]) {
        smallest = rightChild;
    }

    // If the smallest element is not the current root, swap them
    if (smallest != i) {
        swap(arr[i], arr[smallest]);

        // Recursively heapify the affected subtree
        heapifySubtree(arr, n, smallest);
    }
}

void heapify(vector<int>& arr) {
    int n = arr.size();

    // Start from the last non-leaf node and move up to the root
    for (int i = n / 2 - 1; i >= 0; --i) {
        // Heapify the subtree rooted at index i
        heapifySubtree(arr, n, i);
    }
}


vector<int> numberGame(vector<int> &nums) {
    heapify(nums);
    int alice_num;
    int bob_num;
    vector<int> arr;
    while(nums.size()!=0){
        alice_num = nums[0];
        nums.erase(nums.begin());
        heapify(nums);
        bob_num = nums[0];
        nums.erase(nums.begin());
        heapify(nums);
        arr.push_back(bob_num);
        arr.push_back(alice_num);  
    }
    return arr;
};


int main(){
    vector<int> myVector = {5,4,2,3};
    numberGame(myVector);
    return 0;
}
