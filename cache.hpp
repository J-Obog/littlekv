#pragma once
#include "block.hpp"


class Cache {
private:
    int max_sz, _sz, _h, _m; 
    Block* _f, *_b;

public:
    Cache() : max_sz(128), _sz(0), _h(0), _m(0) {};
    Cache(int max_sz) : max_sz(max_sz), _sz(0), _h(0), _m(0) {};
};