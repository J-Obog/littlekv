#pragma once 
#include "CacheBlock.hpp"
#include "Ram.hpp"
#include <iostream>

class LRUCache {
private:
    int size, lines = 0, hits = 0, misses = 0; 
    CacheBlock ** cache;

public:
    LRUCache();
    LRUCache(int size);
    
    CacheBlock * leastRecentlyUsed(); 
    CacheBlock * readFromCache(int address); 
    void writeToCache(int address, int data);
    bool isEmpty();
    bool isFull(); 
    friend std::ostream& operator<<(std::ostream& out, LRUCache& cacheo);
};