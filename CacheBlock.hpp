#pragma once 

class CacheBlock {
private:
    int data;
    int address;
    int hitCounter; 

public:
    CacheBlock(int address, int data) {
        this->address = address; 
        this->data = data; 
        hitCounter = 0; 
    }

    CacheBlock() {
        address = -1; 
        data = 0; 
    }

    int getData() {
        return data; 
    }

    int getAddress() {
        return address; 
    }

    void incrementHitCounter() {
        hitCounter++; 
    }
};