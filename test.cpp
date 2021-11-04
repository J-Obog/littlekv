#include "cache.hpp"
#include <iostream>
#include <ctime>
using namespace std; 


int main() {  
  const int READS = 1000; 
  const int RAM_SIZE = 1040; 
  int ram[RAM_SIZE]; //Dummy RAM
  Cache cache(30); //Cache with max size of 30
  
  srand(time(0));
  
  for(int i = 0; i < RAM_SIZE; i++) //Populate ram with random values
    ram[i] = rand(); 
  
  for(int i = 0; i < READS; i++) {
    int ram_address = rand() % (RAM_SIZE - 1);

    //if(cache.read(ram_address) == nullptr) 
      //cache.write(ram_address, ram[ram_address]); //If not in cache, create new cache block
  }

  
  return 0; 
}