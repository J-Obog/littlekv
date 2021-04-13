#pragma once 
#include "CacheBlock.hpp"
#include "Ram.hpp"

class LRUCache {
private:
    int size, cachePointer, hitCounter, missCounter; 
    Ram * ram; 
    CacheBlock ** cache;
    void evict(); 

public:
    LRUCache();
    LRUCache(int sz);
    void read(int addr);
    void write(int addr, int dat);  
};