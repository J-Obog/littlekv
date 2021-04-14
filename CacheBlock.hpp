#pragma once 

class CacheBlock {
private:
    int data, address, hitCounter = 0; 

public:
    CacheBlock(int addr, int dat);
    CacheBlock();
    int getData(); 
    int getAddress();
    int getHitCounter(); 
    void incrementHitCounter(); 
};