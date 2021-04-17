#pragma once 
#include "block.hpp"
#define MAX_CACHE_SIZE 128

class Cache {
private:
    int max_sz, curr_sz, hits, misses; 
    Block* front, *back;
    void to_front(Block*); 
    void remove(Block*); 

public:
    Cache(); 
    Cache(int);
    void write(int, int);
    Block* read(int);
    int hit_count(); 
    int miss_count(); 
    int size(); 
    int capacity(); 
    double hit_ratio(); 
    double miss_ratio(); 
};