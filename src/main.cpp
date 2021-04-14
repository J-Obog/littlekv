#include "LRUCache.hpp"
#include <iostream>
using namespace std; 


int main() {
  LRUCache cache(20);
  cache.read(0, 50); 
  cache.read(1, 50); 
  cache.read(1, 50);
  cache.read(1, 50);
  cache.read(4, 50);
  cout << cache.getHitRatio() << endl; 
  cout << cache.getMissRatio() << endl; 
  cache.printCache(); 

  return 0; 
}