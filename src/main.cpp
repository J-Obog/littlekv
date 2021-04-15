#include "LRUCache.hpp"
#include <iostream>
#include <vector> 
#include <algorithm>
#include <ctime>
using namespace std; 


int main() {
  const int RAM_SIZE = 20;
  const int READS = 100;


  vector<int> ram(RAM_SIZE);
  srand(time(0));
  std::generate(ram.begin(), ram.end(), rand);

  LRUCache cache(50); 

  for(int i = 0; i < READS; i++) {
    int ram_addr = rand() % (ram.size() - 1); 
    cout << ram_addr << " " << ram[ram_addr] << endl; 
    //cache.read(ram_addr, ram[ram_addr]); 
  } 

  cout << "Entries: " << cache.getCurrentSize() << endl; 
  cout << "Capacity: " << cache.getMaxSize() << endl; 
  cout << "Hits: " << cache.getHitCount() << endl;
  cout << "Misses: " << cache.getMissCount() << endl; 
  cout << "Hit Ratio: " << cache.getHitRatio() * 100 << "%" << endl; 
  cout << "Miss Ratio: " << cache.getMissRatio() * 100 << "%" << endl;   

  return 0; 
}