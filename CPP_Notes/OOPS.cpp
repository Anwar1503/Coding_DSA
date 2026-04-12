#include<iostream>
using namespace std;

class Encapsulation{
private:
    int balance;

public:
    Encapsulation()
    {
        balance = 0; 
    }
    void depositBalance(int amount)
    {
        if(amount>0)
            balance += amount;
    }
    
    int GetBalance()
    {
        return balance;
    }
};

int main(){
    Encapsulation account;
    account.GetBalance();
}
