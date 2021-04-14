#pragma once 
#include "CacheBlock.hpp"
#include <iostream>
#define MAX_CACHE_SIZE 128

class LRUCache {
private:
    int maxSize, currSize = 0, hitCount = 0, missCount = 0; 
    CacheBlock* startBlock = nullptr, *endBlock = nullptr;
    CacheBlock* search(int addr); 
    void updateLRU(CacheBlock* cb); 
    void writeNewBlock(CacheBlock* cb); 

public:
    LRUCache(); 
    LRUCache(int msz);
    void setMaxSize(int msz); 
    void read(int addr, int dat); 
    void printContent(); 
    bool isEmpty(); 
    bool isFull(); 
};