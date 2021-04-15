#include "cache.hpp"
#include <iostream>
#include <vector> 
#include <algorithm>
#include <ctime>
using namespace std; 


int main() {
  const int RAM_SIZE = 100;
  const int READS = 50;

  vector<int> ram(RAM_SIZE);
  srand(time(0));
  std::generate(ram.begin(), ram.end(), rand);

  Cache cache(5); 
  cache.read(0, ram[0]); 
  cache.read(1, ram[1]); 
  cache.read(2, ram[2]); 
  cache.read(3, ram[3]); 
  /*
  for(int i = 0; i < READS; i++) {
    int ram_addr = rand() % (ram.size() - 1); 
    cache.read(ram_addr, ram[ram_addr]); 
  } 
*/
  cout << "Entries: " << cache.entries() << endl; 
  cout << "Capacity: " << cache.capacity() << endl; 
  cout << "Hits: " << cache.hit_count() << endl;
  cout << "Misses: " << cache.miss_count() << endl; 
  cout << "Hit Ratio: " << cache.hit_ratio() * 100 << "%" << endl; 
  cout << "Miss Ratio: " << cache.miss_ratio() * 100 << "%" << endl;   

  return 0; 
}