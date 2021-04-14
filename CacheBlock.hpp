#pragma once 

class CacheBlock {
private:
    int data, address, hits; 
    CacheBlock* next, *prev; 

public:
    CacheBlock(int addr, int dat);
    CacheBlock();
    CacheBlock * getNext(); 
    CacheBlock * getPrev();
    void setNext(CacheBlock * nxt); 
    void setPrev(CacheBlock * prv);
    void incrementHits();   
    bool hasNext(); 
    bool hasPrev(); 
    int getData(); 
    int getAddress();
    int getHits();
};