#include "LRUCache.hpp"
#define MAX_CACHE_SIZE 256

LRUCache::LRUCache() {
    size = MAX_CACHE_SIZE; 
    cache = new CacheBlock * [MAX_CACHE_SIZE];  
}

LRUCache::LRUCache(int size) {
    this->size = size; 
    cache = new CacheBlock * [size];  
}

void LRUCache::writeToCache(int address, int data) {
    if(!isFull()) {
        cache[++lines] = new CacheBlock(address, data); 
    } else {
        CacheBlock * lh = leastRecentlyUsed(); 
        lh = new CacheBlock(address, data);  
    }
}

bool LRUCache::isFull() {
    return lines == (size - 1); 
}

bool LRUCache::isEmpty() {
    return lines == 0; 
}

CacheBlock * LRUCache::readFromCache(int address) {
    for(int i = 0; i < size; i++) {
        if(cache[i]->getAddress() == address) {
            return cache[i]; 
        }
    }
    return nullptr; 
}

CacheBlock * LRUCache::leastRecentlyUsed() {
    if(isEmpty()) {
        return nullptr; 
    }
    CacheBlock * lh = cache[0]; 
    for(int i = 0; i < size; i++) {
        if(cache[i]->getHitCounter() < lh->getHitCounter()) {
            lh = cache[i];  
        }    
    }
    return lh; 
}

std::ostream& operator<<(std::ostream& out, LRUCache& cacheo) {
    out << "Line#\tAddress\tData\tHits";
    for(int i = 0; i < cacheo.size; i++) {
        out << i << '\t' << cacheo.cache[i]->getAddress() 
        << '\t' << cacheo.cache[i]->getData() << '\t' << cacheo.cache[i]->getHitCounter() << '\n'; 
    }   
    return out;
}