#include "LRUCache.hpp"
#include <iostream>
#include <vector> 
#include <algorithm>
#include <ctime>
using namespace std; 


int main() {
  const int RAM_SIZE = 300;
  const int READS = 10;


  vector<int> ram(RAM_SIZE);
  srand(time(0));
  std::generate(ram.begin(), ram.end(), rand);

  LRUCache cache(50); 

  for(int i = 0; i < READS; i++) {
    int ram_addr = rand() % (ram.size() - 1); 
    cout << ram[ram_addr] << endl; 
    //cache.read(ram_addr, ram[ram_addr]); 
  }

  return 0; 
}