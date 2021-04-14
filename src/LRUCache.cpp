#include "LRUCache.hpp"
#include <iostream>

LRUCache::LRUCache() {
    maxSize = MAX_CACHE_SIZE;
}

LRUCache::LRUCache(int sz) {
    maxSize = sz;
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

void LRUCache::setMaxSize(int msz) {
    if(!(msz < maxSize)) {
        maxSize = msz; 
    }
}

void LRUCache::read(int addr, int dat) {
    CacheBlock * p = start; 
    
    while(p != nullptr && p->address != addr) {
        p = p->next; 
    }
    
    if(p != nullptr) {
        hitCount++; 
        updateLRU(p);
    } else {
        missCount++;
        write(addr, dat);
    }
}

void LRUCache::printCache() {
    CacheBlock* p = start; 
    while(start != nullptr) {
        std::cout << p->address << " " << p->data << std::endl; 
        p = p->next; 
    }
}

void LRUCache::write(int addr, int dat) {
    CacheBlock* cb = new CacheBlock(addr, dat); 
    cb->next = start; 
    start = cb; 
    if(isFull()) {
        end = end->prev; 
        delete end->next;
        return; 
    }
    currSize++; 
}

void LRUCache::updateLRU(CacheBlock* cb) {
    if(currSize > 1) {
        if(cb == end) {
            cb->prev->next = nullptr; 
            end = cb->prev; 
            cb->prev = nullptr; 
            cb->next = start;
            start = cb; 
            return; 
        }
        if(cb != start) {
            cb->prev->next = cb->next; 
            cb->next->prev = cb->prev; 
            cb->prev = nullptr; 
            cb->next = start;
            start = cb; 
        }
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