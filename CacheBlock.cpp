#include "CacheBlock.hpp"

CacheBlock::CacheBlock(int address, int data) {
    this->address = address; 
    this->data = data; 
}

CacheBlock::CacheBlock() {
    address = -1; 
    data = 0; 
}

int CacheBlock::getHitCounter() {
    return hitCounter;
}

int CacheBlock::getData() {
    return data; 
}

int CacheBlock::getAddress() {
    return address; 
}

void CacheBlock::incrementHitCounter() {
    hitCounter++; 
}