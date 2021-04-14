#pragma once
#include <string>
#include <iostream>
#define DEFAULT_RAM_SIZE 512

class Ram {
private:
    int size;
    int * ram; 

public:
    Ram();
    Ram(std::string fp); 
    Ram(int sz, std::string fp);
    int operator[] (int idx);
};