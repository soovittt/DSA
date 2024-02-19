#include <iostream>
#include <map>
#include <vector>
#include <unordered_map>
#include <map>
using namespace std;

void printBoard(const vector<vector<int>>& board) {
    for (const auto& row : board) {
        for (int value : row) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
}

void createBoard(vector<vector<int>>& board, int n , vector<vector<int>> obstacles){
    board.assign(n, std::vector<int>(n, 0));
    for (unsigned int i = 0; i < obstacles.size(); i++)
    {
        vector<int> obstacle = obstacles.at(i);
        int row = obstacle[0]-1;
        int col = obstacle[1]-1;
        board[row][col]  = -1;
    }
}


//This is the brute force approach 
int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles) {
    vector<vector<int>> board;
    createBoard(board,n,obstacles);
    int count = 0;
    int temp_c = c_q-1;
    int temp_r = r_q-1;
    //go to right
    temp_c++;
    while(temp_c <= n-1 && board[temp_r][temp_c] != -1  ){
        count++;
        temp_c++;
        if(temp_c >= n){
            break;
        }
    }
    //go to left 
    temp_c = c_q-1;
    temp_r = r_q-1;
    temp_c--;
    while(temp_c >= 0 && board[temp_r][temp_c] != -1  ){
        count++;
        temp_c--;
        if(temp_c < 0){
            break;
        }
    }

    //go up
    temp_c = c_q-1;
    temp_r = r_q-1;
    temp_r--;
    while(temp_r >= 0 && board[temp_r][temp_c] != -1 ){
        count++;
        temp_r--;
        if(temp_r < 0){
            break;
        }
    }

    //go down
    temp_c = c_q-1;
    temp_r = r_q-1;
    temp_r++;
    while(temp_r <= n-1 && board[temp_r][temp_c] != -1  ){
        count++;
        temp_r++;
        if(temp_r>=n){
            break;
        }
    }

    // go diagonals (top right and bottom right)
    temp_c = c_q-1;
    temp_r = r_q-1;
    temp_c++;
    temp_r--;
    while(temp_r <= n-1 && temp_c <= n-1 && board[temp_r][temp_c] != -1){
        count++;
        temp_r--;
        temp_c++;
        if(temp_r>=n || temp_c >=n){
            break;
        }
    }

        temp_c = c_q-1;
    temp_r = r_q-1;
    temp_c++;
    temp_r++;
    while(temp_r <= n-1 && temp_c <= n-1 && board[temp_r][temp_c] != -1 ){
        count++;
        temp_r++;
        temp_c++;
        if(temp_r>=n || temp_c >=n){
            break;
        }
    }



    // go diagonal (top left and bottom left)
        temp_c = c_q-1;
    temp_r = r_q-1;
    temp_c--;
    temp_r--;
    while(temp_r >= 0  && temp_c >= 0 && board[temp_r][temp_c] != -1 ){
        count++;
        temp_r--;
        temp_c--;
        if(temp_r < 0 || temp_c < 0){
            break;
        }
    }
    temp_c = c_q-1;
    temp_r = r_q-1;
    temp_r++;
    temp_c--;
    while(temp_r < n  && temp_c >= 0 && board[temp_r][temp_c] != -1 ){
        count++;
        temp_r++;
        temp_c--;
        if(temp_r >= n || temp_c < 0){
            break;
        }
    }
    return count;  
}


int main(){
int n, k, r_q, c_q;
    cin >> n >> k >> r_q >> c_q;

    vector<vector<int>> obstacles(k, vector<int>(2, 0));

    for (int i = 0; i < k; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> obstacles[i][j];
        }
    }

    int result = queensAttack(n, k, r_q, c_q, obstacles);

    cout << result << endl;

    return 0;
}




//    //when queen goes right 
//     int temp_r = r_q;
//     int temp_c = c_q;
//     int count = 0;

//     while(temp_c != n){
//         for (unsigned int i = 0; i < obstacles.size(); i++)
//         {
//             if(obstacles[i][0]==temp_r && obstacles[i][1]==temp_c ){

//             }else{
//                 count++;
//                 temp_c++;
//             }
//         }
//     }
//     std::cout<<"count : "<<count<<std::endl;
//     temp_r = r_q;
//     temp_c = c_q;

//     //when queen goes left 
//     std::cout<<"r : "<<temp_r<<" c_q : "<<temp_c<<std::endl;
//     while(temp_c != 0){
//         for (unsigned int i = 0; i < obstacles.size(); i++)
//         {
//             if(obstacles[i][0]==temp_r && obstacles[i][1]==temp_c ){
//                 break;
//             }else{
//                 count++;
//                 temp_c--;
//             }
//         }
//     }
//             temp_r = r_q;
//         temp_c = c_q;
//     //when queen goes up 
//     //when queen goes down
//     //when queen up right diagonal
//     //when queen goes up left diagonal
//     //when queen goes down left diagonal
//     //when queen goes down right  diagonal
//     std::cout<<count<<std::endl;