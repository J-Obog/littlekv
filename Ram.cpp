#include "Ram.hpp"
#include <fstream>

Ram::Ram(std::string filePath) {
    size = MAX_RAM_SIZE;
    ram = new int[MAX_RAM_SIZE]; 

    std::ifstream ramFile(filePath); 
    int c = 0; 

    while(ramFile >> ram[c])
        c++; 
}

int Ram::operator[](int index) {
    return ram[index]; 
}

std::ostream& operator<<(std::ostream& out, Ram& ramO) {
    out << "Address\tData\n";
    for(int i = 0; i < ramO.size; i++) {
        out << i << '\t' << ramO[i] << '\n'; 
    }
    return out; 
}