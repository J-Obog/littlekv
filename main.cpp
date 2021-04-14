#include <iostream> 
#include "Ram.hpp"
#include "LRUCache.hpp"
using namespace std; 


int main() {
  //Ram ram("image.ram");
  LRUCache cache(20); 
  cout << cache;  
  //cout << ram;  

  return 0; 
}