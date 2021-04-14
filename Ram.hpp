#pragma once
#include <string>
#include <iostream>

class Ram {
private:
    int size; 
    int * ram; 

public:
    Ram(); 
    Ram(int sz); 
    Ram(int sz, int * arr); 
    int operator[] (int idx);
    friend std::ostream& operator<<(std::ostream& out, Ram& ramref);
};