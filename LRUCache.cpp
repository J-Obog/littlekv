#include "LRUCache.hpp"
#define MAX_RAM_SIZE 256

LRUCache::LRUCache() {
    size = MAX_RAM_SIZE; 
    cache = new CacheBlock*[MAX_RAM_SIZE];  
}

LRUCache::LRUCache(int size) {
    this->size = size; 
    cache = new CacheBlock*[size];  
}

void LRUCache::write(int address, int data) {
    
}

void LRUCache::read(int address) {
    for(int i = 0; i < size; i++) {
        if(cache[i]->getAddress() == address) {
             hitCounter++; 
             cache[i]->incrementHitCounter(); 
             return; 
        }
    }
    missCounter++; 
    write(address, (*ram)[address]); 
}