#include "CacheBlock.hpp"

CacheBlock::CacheBlock(int addr, int dat) {
    address = addr; 
    data = dat;
    hits = 0; 
    next = nullptr; 
    prev = nullptr;  
};

CacheBlock::CacheBlock() {
    address = -1; 
    data = 0; 
    hits = 0; 
    next = nullptr; 
    prev = nullptr;   
};

CacheBlock * CacheBlock::getNext() {
    return next; 
}; 

CacheBlock * CacheBlock::getPrev() {
    return prev; 
};

void CacheBlock::setNext(CacheBlock * nxt) {
    if(nxt == nullptr) {
        next = nullptr;
    } else {
        next = nxt; 
    }
}; 

void CacheBlock::setPrev(CacheBlock * prv) {
    if(prv == nullptr) {
        prev = nullptr;
    } else {
        prev = prv; 
    }
};

void CacheBlock::incrementHits() {
    hits++; 
};   

bool CacheBlock::hasNext() {
    return !(next == nullptr); 
}; 

bool CacheBlock::hasPrev() {
    return !(prev == nullptr);
}; 

int CacheBlock::getData() {
    return data; 
}; 

int CacheBlock::getAddress() {
    return address;
};

int CacheBlock::getHits() {
    return hits; 
};