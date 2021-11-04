#pragma once

struct Block {
    int data; 
    Block* next, *prev;

    Block(int data) {
        this->data = data; 
        next = prev = nullptr; 
    }
};