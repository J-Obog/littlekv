#pragma once
#include <string>
#include <iostream>
#define MAX_RAM_SIZE 512

class Ram {
private:
    int size;
    int * ram; 

public:
    Ram(std::string fp); 
    int operator[] (int idx);
    friend std::ostream& operator<<(std::ostream& out, Ram& r);
};