#include "Cache.h"
#include <iostream>
#include <ctime>
#define RAM_SIZE 1040
#define READS 1000
using namespace std; 


int main() {  
  int ram[RAM_SIZE]; //Dummy RAM
  Cache cache(30); //Cache with max size of 30
  
  srand(time(0));
  
  for(int i = 0; i < RAM_SIZE; i++) //Populate ram with random values
    ram[i] = rand(); 
  
  for(int i = 0; i < READS; i++) {
    int ram_address = rand() % (RAM_SIZE - 1);

    if(cache.read(ram_address) == nullptr) 
      cache.write(ram_address, ram[ram_address]); //If not in cache, create new cache block
  }

  //Output cache stats
  cout << "Entries: " << cache.size() << endl; 
  cout << "Hits: " << cache.hit_count() << endl; 
  cout << "Misses: " << cache.miss_count() << endl;   
  cout << "Hit Ratio: " << cache.hit_ratio() * 100 << "%" << endl; 
  cout << "Miss Ratio: " << cache.miss_ratio() * 100 << "%" << endl;

  return 0; 
}