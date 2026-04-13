//Race condition,deadlocks

#include<iostream>
#include<thread>

using namespace std;

void function1(char symbol){
    for(int i =0;i<200;i++){
        std::cout<<symbol;
    }
}

void function2(){
    int i =0;
    while(i < 300){
        std::cout<<"return basha";
        i++;
    }
}

int main(){
    std::thread worker1(function1,'o');
    std::thread worker2(function2);
    return 0;
}