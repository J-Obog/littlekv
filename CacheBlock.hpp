#pragma once 
#include "LRUCache.hpp"

class CacheBlock {
friend class LRUCache; 
private:
    int data, address; 
    CacheBlock* next = nullptr, *prev = nullptr; 

public:
    CacheBlock(int addr, int dat);
    CacheBlock();
};