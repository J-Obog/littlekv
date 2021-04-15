#pragma once 
#include "block.hpp"
#define MAX_CACHE_SIZE 128

class Cache {
private:
    int max_sz, curr_sz, hits, misses; 
    Block* front, *back;
    void insertBlock(Block*); 
    void moveToFront(Block*); 
    
public:
    Cache(); 
    Cache(int);
    void set_capacity(int); 
    void read(int, int); 
    int hit_count(); 
    int miss_count(); 
    int entries(); 
    int capacity(); 
    bool is_empty(); 
    bool is_full(); 
    double hit_ratio(); 
    double miss_ratio();
};