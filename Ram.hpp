#pragma once
#include <string>

class Ram {
private:
    int size; 
    int * ram; 

public:
    Ram(); 
    Ram(int sz); 
    Ram(int sz, int * arr); 
    int operator[] (int idx);
};