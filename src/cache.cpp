#include "cache.hpp"

Cache::Cache() {
    front = back = nullptr; 
    max_sz = MAX_CACHE_SIZE;
    hits = misses = curr_sz = 0;
}

Cache::Cache(int max) {
    front = back = nullptr; 
    max_sz = max;
    hits = misses = curr_sz = 0;
}

int Cache::hit_count() {
    return hits; 
}

int Cache::miss_count() {
    return misses; 
} 

int Cache::entries() {
    return curr_sz; 
}

int Cache::capacity() {
    return max_sz; 
}

void Cache::set_capacity(int max) {
    if(!(max < curr_sz)) {
        max_sz = max; 
    }
}

void Cache::insertBlock(Block* cb) {
    if(is_empty()) {
        front = cb; 
        back = cb; 
    } else {
        cb->next = front; 
        front->prev = cb; 
        front = cb; 
        if(is_full()) {
            back = back->prev; 
            delete back->next; 
            curr_sz--; 
        }
    }
    curr_sz++; 
}


void Cache::moveToFront(Block* cb) {
    if(cb->prev == nullptr) {
        return; 
    } else if(cb->next == nullptr) {
        back = back->prev; 
        back->next = nullptr;   
    } else {
        cb->prev->next = cb->next; 
        cb->next->prev = cb->prev; 
    }
    
    cb->next = front; 
    front->prev = cb; 
    cb->prev = nullptr;
    front = cb; 
} 

void Cache::read(int address, int data) {
    Block* itr = front; 
    while(itr != nullptr) {
        if(itr->address == address) {
            hits++; 
            moveToFront(itr); 
            return; 
        }
        itr = itr->next; 
    }
    misses++; 
    insertBlock(new Block(address, data)); 
}

bool Cache::is_full() {
    return curr_sz >= max_sz; 
}

bool Cache::is_empty() {
    return curr_sz == 0; 
}

double Cache::hit_ratio() {
    return hits / (double)(hits + misses); 
}

double Cache::miss_ratio() {
    return misses / (double)(hits + misses); 
}