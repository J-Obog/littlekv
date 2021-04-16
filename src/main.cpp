#include "cache.hpp"
#include <iostream>
#include <ctime>
using namespace std; 


int main() {
  Cache cache(3); 

  for(int i = 0; i < 50; i++) {
    if(cache.read(i) != nullptr) {
      cout << "Cache Hit" << endl; 
    } else {
      cout << "Cache Miss" << endl; 
      cache.write(i, 1); 
    }
  }

  return 0; 
}