#include "CacheBlock.hpp"

CacheBlock::CacheBlock(int ramAdress, int addressData) {
    address = ramAdress; 
    data = addressData;
};

CacheBlock::CacheBlock() {
    address = -1; 
    data = 0; 
};