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
        hits++; 
        b->data = data; 
        remove(b);
        to_front(b); 
    } else {
        misses++; 
        Block* nb = new Block(address, data); 
        if(curr_sz == max_sz) {
            Block* tmp = back;
            back = back->prev;
            back->next = nullptr; 
            delete tmp; 
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
        hits++; 
        remove(itr);
        to_front(itr);  
    } 
    return itr;
}

int Cache::hit_count() {
    return hits; 
}

int Cache::miss_count() {
    return misses; 
} 

int Cache::size() {
    return curr_sz; 
} 

int Cache::capacity() {
    return max_sz;     
}

double Cache::hit_ratio() {
    return hits / (double) (hits + misses);
}

double Cache::miss_ratio() {
  return misses / (double) (hits + misses);
} 