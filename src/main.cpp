#include "cache.hpp"
#include <iostream>
#include <ctime>
#define RAM_SIZE 100
#define READS 1000
using namespace std; 




int main() {
  
  int ram[RAM_SIZE];
  Cache cache(30);
  
  srand(time(0));
  
  for(int i = 0; i < RAM_SIZE; i++) //Populate ram with random values
    ram[i] = rand(); 
  
  
  for(int i = 0; i < READS; i++) {
    int ram_address = rand() % (RAM_SIZE - 1);

    if(cache.read(ram_address) == nullptr) 
      cache.write(ram_address, ram[ram_address]); 
  }

  cout << "Entries: " << cache.size() << endl; 
  cout << "Hits: " << cache.hit_count() << endl; 
  cout << "Misses: " << cache.miss_count() << endl;   

  return 0; 
}