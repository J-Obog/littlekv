#include "LRUCache.hpp"

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
        cache[++curr] = new CacheBlock(address, data); 
    } else {
        CacheBlock * lh = leastRecentlyUsed(); 
        lh = new CacheBlock(address, data);  
    }
}

double LRUCache::hitRatio() {
    return hits / (double)(hits + misses); 
}

bool LRUCache::isFull() {
    return curr == (size - 1); 
}

bool LRUCache::isEmpty() {
    return curr == 0; 
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

std::ostream& operator<<(std::ostream& out, LRUCache& cacheO) {
    const double hr = cacheO.hitRatio(); 
    out << "Hit Ratio: " << hr << '\n';
    out << "Miss Ratio: " << (1 - hr) << '\n';
    out << "Content ..." << '\n'; 
    for(int i = 0; i < cacheO.size; i++) {
        out << "[" << i << "]: " << cacheO;  
    }   
    return out;
}