#include "Ram.hpp"
#include <fstream>

Ram::Ram() {
    size = DEFAULT_RAM_SIZE;
    ram = new int[DEFAULT_RAM_SIZE];

    //randomize addresses
}

Ram::Ram(std::string filePath) {
    size = DEFAULT_RAM_SIZE;
    ram = new int[DEFAULT_RAM_SIZE]; 

    std::ifstream ramFile(filePath); 
    int c = 0; 

    while(ramFile >> ram[c])
        c++; 
}

Ram::Ram(int size, std::string filePath) {
    this->size = size;
    ram = new int[size]; 

    std::ifstream ramFile(filePath); 
    int c = 0; 

    while(ramFile >> ram[c])
        c++; 
}

int Ram::operator[](int index) {
    return ram[index]; 
}
