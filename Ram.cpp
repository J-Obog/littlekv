#include "Ram.hpp"
#include <random>
#define MAX_RAM_SIZE 1040
#define MIN_DATA_VAL -2147483647
#define MAX_DATA_VAL 2147483646

int randNum(int a, int b) {
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(a, b);
    return distribution(generator);
}

Ram::Ram() {
    size = MAX_RAM_SIZE; 
    ram = new int[size]; 

    for(int i = 0; i < size; i++) {
        ram[i] = randNum(MIN_DATA_VAL, MAX_DATA_VAL); 
    }
}

Ram::Ram(int size) {
    this->size = size; 
    ram = new int[size]; 

    for(int i = 0; i < size; i++) {
        ram[i] = randNum(MIN_DATA_VAL, MAX_DATA_VAL); 
    }
}

Ram::Ram(int size, int * array) {
    this->size = size; 
    ram = new int[size]; 

    for(int i = 0; i < size; i++) {
        ram[i] = array[i]; 
    } 
}

int Ram::operator[](int address) {
    return ram[address]; 
} 