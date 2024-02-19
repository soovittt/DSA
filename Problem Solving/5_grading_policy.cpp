#include <iostream>
#include <vector>

using namespace std;

int check_5_multiple(int number){return number + (5 - (number % 5));}

template<typename T>
void printVector(const std::vector<T>& vec) {
    for (const auto& element : vec) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}


vector<int> gradingStudents(vector<int> grades) {
  vector<int> graded;
  for (unsigned int i = 0; i < grades.size(); i++) {
    
    int next = check_5_multiple(grades[i]);
    if (grades[i] < 38) {
        graded.push_back(grades[i]);
    } else if (grades[i] >= 38) {
      if (next - grades[i] < 3) {
        graded.push_back(next);
      } else {
        graded.push_back(grades[i]);
      }
    }
  }
  return graded;
}

int main() {
  vector<int> grades = {73, 67, 38, 38, 91, 50};
  vector<int> v = gradingStudents(grades);
  printVector(v);
  return 0;
}