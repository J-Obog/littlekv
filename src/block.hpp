#pragma once 

class Block {
public:
    int data; 
    int address; 
    Block* next;
    Block* prev; 
    
    Block(int address, int data) {
        this->data = data; 
        this->address = address; 
        next = prev = nullptr; 
    }
};