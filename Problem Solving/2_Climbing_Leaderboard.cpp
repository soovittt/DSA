#include <iostream>
#include <map>
#include <vector>
#include <unordered_map>
#include <map>


template <typename KeyType, typename ValueType>
void printMap(const std::unordered_map<KeyType, ValueType> &myMap) {
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



std::vector<int> climbingLeaderboard_bruteforce(std::vector<int> ranked,
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


std::vector<int> climbingLeaderboard_efficient(std::vector<int> ranked,
                                     std::vector<int> player) {
  int rank = 1;
  int top = ranked[0];
  std::unordered_map<int, int> rank_map = {};
  std::vector<int> rank_vector;
  rank_vector.push_back(top);
  
  for (unsigned int i = 0; i < ranked.size(); i++) {
    if (ranked[i] == top) {
    } else if (ranked[i] < top) {
      top = ranked[i];
      rank++;
      rank_vector.push_back(ranked[i]);
    }
  }
  std::cout<<rank_vector.size()<<std::endl;
  std::vector<int> final;
  for (unsigned int i = 0; i < player.size(); i++)
  {
      int score = player[i];
      int start = 0;
      int end = rank_vector.size()-1;
      int found = -1;
      while (end >= start)
      {
        int mid = (start+end)/2;
        if(rank_vector[mid]==score){
          final.push_back(mid+1);
          break;
        }else if(rank_vector[mid] > score){
          start = mid + 1;
        }else if(rank_vector[mid] < score){
          end = mid - 1;
        }
      }
      if(end < start){
        final.push_back(end+2);
      }
  }
  return final;
}



















int main() {
std::vector<int> ranked1 = {100, 100, 50, 40, 40, 20, 10};
std::vector<int> player1 = {5, 25, 50, 120};
  climbingLeaderboard_efficient(ranked1, player1);
  return 0;
}