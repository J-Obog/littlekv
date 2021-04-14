#include <iostream> 
#include "Ram.hpp"
#include "LRUCache.hpp"
#include "CacheBlock.hpp"
using namespace std; 


int main() {
  LRUCache cache(20);
  cache.read(0, 50); 
  cache.printContent(); 
  
  return 0; 
}