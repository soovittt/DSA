#include <iostream>
#include <map>
#include <vector>
#include <unordered_map>
#include <map>




using namespace std;
class BigInt{
    string digits;
    public:
        //constructors
        BigInt(unsigned long long n = 0 );
        BigInt(string &s);
        BigInt(const char* c);
        BigInt(BigInt &b);

        friend BigInt &operator*=(BigInt &, const BigInt &);
        friend BigInt operator*(const BigInt &, const BigInt &);



        
};


int main(){
    return 0;
}