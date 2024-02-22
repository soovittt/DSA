#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int hourglassSum(vector<vector<int>> arr) {
  int max;
  vector<int> sum_vec;
  for (unsigned int r = 0; r < 4; r++) {
    int sum = 0;
    for (unsigned int c = 0 ; c <  4; c++) {
      int a = arr[r][c];
      int b = arr[r][c + 1];
      int c_ = arr[r][c + 2];
      int d = arr[r + 1][c + 1];
      int e = arr[r + 2][c];
      int f = arr[r + 2][c + 1];
      int g = arr[r + 2][c + 2];
      sum = a+b+c_+d+e+f+g;
      sum_vec.push_back(sum);
    }
  }
  return *(std::max_element(sum_vec.begin(),sum_vec.end()));
}

int main() {
  vector<vector<int>> myMatrix = {{-9, -9, -9, 1, 1, 1}, {0, -9, 0, 4, 3, 2},
                                  {-9, -9, -9, 1, 2, 3}, {0, 0, 8, 6, 6, 0},
                                  {0, 0, 0, -2, 0, 0},   {0, 0, 1, 2, 4, 0}};
  std::cout<<hourglassSum(myMatrix)<<std::endl;
  return 0;
}
