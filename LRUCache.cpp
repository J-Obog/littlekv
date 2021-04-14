#include "LRUCache.hpp"

LRUCache::LRUCache() {
    maxSize = MAX_CACHE_SIZE;
}

LRUCache::LRUCache(int sz) {
    maxSize = sz;
}

CacheBlock* LRUCache::search(int addr) {
    CacheBlock * tmp = startBlock; 
    while(tmp != nullptr && tmp->address != addr) {
        tmp = tmp->next; 
    }
    return tmp; 
}
void LRUCache::printContent() {
    CacheBlock* tmp = startBlock; 
    int c = 0; 
    while(tmp != nullptr) {
        std::cout << "[" << c << "]" << std::endl;  
        tmp = tmp->next; 
        c++; 
    }
}

void LRUCache::read(int addr, int dat) {
    CacheBlock* q = search(addr); 
    if(q != nullptr) {
        updateLRU(q);
    } else {
        CacheBlock* cb = new CacheBlock(addr, dat); 
        writeNewBlock(cb);
    }
}

void LRUCache::writeNewBlock(CacheBlock* cb) {
    if(isEmpty()) {
        currSize++;
        startBlock = cb; 
        endBlock = cb; 
        return; 
    }

    if(isFull()) {
        endBlock = endBlock->prev;
        delete endBlock->next;
        startBlock->prev = cb; 
        cb->next = startBlock; 
        return; 
    }

    currSize++; 
    startBlock->prev = cb; 
    cb->next = startBlock; 
    startBlock = cb; 
}

void LRUCache::updateLRU(CacheBlock* cb) {
    if(currSize > 1) {
        if(cb == endBlock) {
            cb->prev->next = nullptr; 
            endBlock = cb->prev; 
            cb->prev = nullptr; 
            cb->next = startBlock;
            startBlock = cb; 
            return; 
        }
        if(cb != startBlock) {
            cb->prev->next = cb->next; 
            cb->next->prev = cb->prev; 
            cb->prev = nullptr; 
            cb->next = startBlock;
            startBlock = cb; 
        }
    }
}


bool LRUCache::isFull() {
    return currSize == (maxSize - 1); 
}

bool LRUCache::isEmpty() {
    return currSize = 0; 
}

