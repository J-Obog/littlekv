#include "cache.hpp"

Cache::Cache() {
    max_sz = MAX_CACHE_SIZE; 
    misses = hits = curr_sz = 0; 
    front = back = nullptr; 
} 

Cache::Cache(int size) {
    max_sz = size; 
    misses = hits = curr_sz = 0; 
    front = back = nullptr;
}

void Cache::remove(Block* b) { 
    if(b->prev != nullptr) {
        b->prev->next = b->next; 
    } else {
        front = b->next; 
    }

    if(b->next != nullptr) {
        b->next->prev = b->prev; 
    } else {
        back = b->prev; 
    }   
}

void Cache::to_front(Block* b) {
    b->prev = nullptr;
    b->next = front; 

    if(front != nullptr)
        front->prev = b; 

    front = b; 

    if(back == nullptr) 
        back = b; 
}

void Cache::write(int address, int data) {
    Block* b = read(address);

    if(b != nullptr) {
        b->data = data; 
        remove(b);
        to_front(b); 
    } else {
        Block* nb = new Block(address, data); 
        if(curr_sz == max_sz) {
            back = back->prev; 
            delete back->next;     
        } else {
            curr_sz++; 
        }
        to_front(nb);    
    }
}

Block* Cache::read(int address) {
    Block* itr = front; 

    while(itr != nullptr && itr->address != address)
        itr = itr->next; 
    
    if(itr != nullptr) {
        remove(itr);
        to_front(itr);  
    } 
    return itr; 
}