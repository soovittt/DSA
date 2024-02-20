#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


string organizingContainers(vector<vector<int>> container) {
    int n = container.size();
    vector<int> row(n,0);
    vector<int> col(n,0);
    
    for (unsigned int i = 0; i < n; i++)
    {
        for (unsigned int j = 0; j < n; j++)
        {
            row[i] += container[i][j];
            col[i] += container[j][i];       
        }
    }
    std::sort(row.begin(), row.end());
    std::sort(col.begin(), col.end());

    if(row==col){
        return "Possible";
    }
    return "Impossible";
}

int main(){
    std::vector<std::vector<int>> container = {{1, 4}, {2, 3}};
    std::cout<<organizingContainers(container)<<std::endl;
    return 0;
}