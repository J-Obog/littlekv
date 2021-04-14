#include "CacheBlock.hpp"

CacheBlock::CacheBlock(int addr, int dat) {
    address = addr; 
    data = dat;
};

CacheBlock::CacheBlock() {
    address = -1; 
    data = 0; 
};
