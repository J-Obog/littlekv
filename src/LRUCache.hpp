#pragma once 
#include "CacheBlock.hpp"
#define MAX_CACHE_SIZE 128

class LRUCache {
private:
    int maxSize; 
    int currSize = 0;
    int hitCount = 0; 
    int missCount = 0; 
    CacheBlock* frontBlock = nullptr;
    CacheBlock* backBlock = nullptr;
    void popBlock(); 
    void insertBlock(int ramAddress, int addressData); 
    void moveToFront(CacheBlock* cacheBlock); 
    
public:
    LRUCache(); 
    LRUCache(int maxCacheSize);
    void setMaxSize(int maxCacheSize); 
    int getHitCount(); 
    int getMissCount(); 
    int getCurrentSize(); 
    int getMaxSize(); 
    bool isEmpty(); 
    bool isFull(); 
    double getHitRatio(); 
    double getMissRatio();
};