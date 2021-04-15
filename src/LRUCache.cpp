#include "LRUCache.hpp"

LRUCache::LRUCache() {
    maxSize = MAX_CACHE_SIZE;
}

LRUCache::LRUCache(int maxCacheSize) {
    maxSize = maxCacheSize;
}

int LRUCache::getHitCount() {
    return hitCount; 
}

int LRUCache::getMissCount() {
    return missCount; 
} 

int LRUCache::getCurrentSize() {
    return currSize; 
}

int LRUCache::getMaxSize() {
    return maxSize; 
}

void LRUCache::setMaxSize(int maxCacheSize) {
    if(!(maxCacheSize < maxSize)) {
        maxSize = maxCacheSize; 
    }
}

void LRUCache::popBlock() {
    backBlock = backBlock->prev;
    delete backBlock->next;   
    currSize--; 
}

void LRUCache::insertBlock(int ramAddress, int addressData) {
    CacheBlock* newBlock = new CacheBlock(ramAddress, addressData);
    newBlock->next = frontBlock; 
    frontBlock->prev = newBlock; 
    frontBlock = newBlock; 
    currSize++; 
}

void LRUCache::moveToFront(CacheBlock* cacheBlock) {
    if(cacheBlock == frontBlock)
        return; 

    if(cacheBlock == backBlock) {
        backBlock = backBlock->prev; 
        backBlock->next = nullptr; 
    }

    if(cacheBlock->next != nullptr) {
        
    }
} 

bool LRUCache::isFull() {
    return currSize == (maxSize - 1); 
}

bool LRUCache::isEmpty() {
    return currSize = 0; 
}

double LRUCache::getHitRatio() {
    return hitCount / (double)(hitCount + missCount); 
}

double LRUCache::getMissRatio() {
    return missCount / (double)(hitCount + missCount); 
}