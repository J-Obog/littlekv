#pragma once
#include "CacheBlock.hpp"

class LRUCache {
private:
    int size; 
    int * ram; 
    CacheBlock ** cache; 
    int basePointer = 0; 
    int hitCounter = 0;
    int missCounter = 0;  

public:
    LRUCache(int * ram, int size = 128) {
        this->ram = ram; 
        this->size = size;
        cache = new CacheBlock * [size]; 
    }

    void writeToCache(int address) {

    }

    void readFromCache(int address) {
        for(int i = 0; i < size; i++) {
            if(cache[i]->getData() == address) {
                hitCounter++; 
                cache[i]->incrementHitCounter(); 
                return; 
            }
        }
        missCounter++; 
        writeToCache(address); 
    }

    double hitRatio() {
        return hitCounter / (double)(hitCounter+missCounter); 
    }

    double missRatio() {
        return 1 - hitRatio(); 
    }

};