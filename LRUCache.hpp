#pragma once 
#include "CacheBlock.hpp"

class LRUCache {
private:
    int size, curr, hits, misses; 
    CacheBlock * head, tail;

public:
    LRUCache();
    LRUCache(int sz);
    //LRUCache(std::string fn); 
    //LRUCache(int sz, std::string fn); 
    CacheBlock * leastRecentlyUsed(); 
    CacheBlock * readFromCache(int addr); 
    double hitRatio(); 
    void writeToCache(int addr, int dat);
    bool isEmpty();
    bool isFull(); 
    friend std::ostream& operator<<(std::ostream& out, LRUCache& cacheO);
};