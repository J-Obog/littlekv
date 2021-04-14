#pragma once 
#include "CacheBlock.hpp"
#include <iostream>
#define MAX_CACHE_SIZE 128

class LRUCache {
private:
    int maxSize; 
    int currSize = 0;
    int hitCount = 0; 
    int missCount = 0; 
    CacheBlock* start = nullptr;
    CacheBlock* end = nullptr;
    void updateLRU(CacheBlock* cb); 
    void write(int addr, int dat); 

public:
    LRUCache(); 
    LRUCache(int msz);
    void setMaxSize(int msz); 
    void read(int addr, int dat);
    int getHitCount(); 
    int getMissCount(); 
    int getCurrentSize(); 
    int getMaxSize(); 
    bool isEmpty(); 
    bool isFull(); 
    double getHitRatio(); 
    double getMissRatio();
};