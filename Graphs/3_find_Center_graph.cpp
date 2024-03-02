#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool keyExists(const map<int, string>& myMap, int key) {
    return myMap.find(key) != myMap.end();
}

int findCenter(vector<vector<int>>& edges) {
    map<int, vector<int>> adjacencyList;

    // Create an adjacency list using the given edges
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];

        adjacencyList[u].push_back(v);
        adjacencyList[v].push_back(u);
    }

    int center = 0;

    // Iterate through the adjacency list and find the center
    for (auto it = adjacencyList.begin(); it != adjacencyList.end(); ++it) {
        if (it->second.size() == adjacencyList.size() - 1) {
            center = it->first;
            return center;
        }
    }

    return -1;
}

int main() {
    // Test the findCenter function
    vector<vector<int>> edges = {{1, 2}, {2, 3}, {4, 2}};
    int center = findCenter(edges);

    if (center != -1) {
        cout << "Center: " << center << endl;
    } else {
        cout << "No center found." << endl;
    }

    return 0;
}



int main(){

    return 0;
}