#pragma once 

class CacheBlock {
friend class LRUCache; 
private:
    int data; 
    int address; 
    CacheBlock* next = nullptr;
    CacheBlock* prev = nullptr; 

public:
    CacheBlock(int ramAddres, int addressData);
    CacheBlock();
};