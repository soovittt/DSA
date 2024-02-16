#include <iostream>
#include <map>
#include <vector>
#include <unordered_map>
#include <map>
template <typename KeyType, typename ValueType>
void printMap(const std::map<KeyType, ValueType> &myMap) {
  for (const auto &pair : myMap) {
    std::cout << "Key: " << pair.first << ", Value: " << pair.second
              << std::endl;
  }
}

template<typename T>
void printVector(const std::vector<T>& vec) {
    for (const auto& element : vec) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}



std::vector<int> climbingLeaderboard(std::vector<int> ranked,
                                     std::vector<int> player) {
  int rank = 1;
  int top = ranked[0];
  std::map<int, int> rank_map = {};
  for (unsigned int i = 0; i < ranked.size(); i++) {
    if (ranked[i] == top) {
      rank_map.insert(std::make_pair(ranked[i],rank));
    } else if (ranked[i] < top) {
      top = ranked[i];
      rank++;
      rank_map.insert(std::make_pair(ranked[i],rank));
    }
  }
  std::vector<int> final;
  for (unsigned int i = 0; i < player.size(); i++) {
    int score = player[i];
    int temp_rank = rank;
    int inserted = -1;
    for (auto rit = rank_map.rbegin(); rit != rank_map.rend(); ++rit) {
        if(score > rit->first){
            final.push_back(rank_map[rit->first]);
            inserted = 1;
            break;
        }
        if(score==rit->first){
            final.push_back(rank_map[rit->first]);
            inserted = 1;
            break;
        }
    }
    if(inserted == -1){
     temp_rank++;
        final.push_back(temp_rank);
    }
  }
}

int main() {
  std::vector<int> ranked = {100,100,50,40,40,20,10};

  // Declare and initialize the "player" vector
  std::vector<int> player ={5,25,50,120};
  climbingLeaderboard(ranked, player);
  return 0;
}