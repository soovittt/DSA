#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> rotateLeft(int d, vector<int> arr) {
    // for i in d 
    //  move the element one place front 
    d = d % arr.size();
    for (unsigned int i = 0; i < d; i++)
    {   
        int temp = arr[0];
        for (unsigned int i = 0; i < arr.size() - 1; i++)
        {
            arr[i] = arr[i+1];
        }
        arr[arr.size()-1] = temp;
    }
    return arr;
}


int main(){
    return 0;
}