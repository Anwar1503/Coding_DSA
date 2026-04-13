#include<iostream>
#include<thread>
#include<map>
#include<string>
#include<chrono>
using namespace std::chrono_literals;

void RefreshForecast(std::map<std::string,int> &forecastMap){
    while(true){
        for(auto &iter: forecastMap){
            iter.second ++;

        }
        std::this_thread::sleep_for(2000ms);
    }

}


int main(){
    std::map<std::string, int> forecastMap = {
        {"Mumbai",40},
        {"Hyderabad",42},
        {"Banglore",38}
    };

    std::thread workitem(RefreshForecast,std::ref(forecastMap));
    workitem.join();

    return 0;
}