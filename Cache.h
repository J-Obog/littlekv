#ifndef CACHE_H
#define CACHE_H 
#include "Block.h"
#define MAX_CACHE_SIZE 128

class Cache {
private:
    int max_sz, curr_sz, hits, misses; 
    Block* front, *back;
    void to_front(Block*); 
    void remove(Block*); 

public:
    Cache(); 
    Cache(int);
    void write(int, int);
    Block* read(int);
    int hit_count(); 
    int miss_count(); 
    int size(); 
    int capacity(); 
    double hit_ratio(); 
    double miss_ratio();
    bool is_full(); 
    bool is_empty();  
};

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
            back = back->prev;
            delete back->next; 
            back->next = nullptr; 
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

bool Cache::is_empty() {
    return curr_sz == 0; 
}

bool Cache::is_full() {
    return curr_sz >= max_sz; 
}

#endif