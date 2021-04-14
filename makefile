output: main.o block.o lru.o 
	g++ -c main.o block.o lru.o -o outputs 

main.o: main.cpp
	g++ -c main.cpp

block.o: CacheBlock.cpp CacheBlock.hpp
	g++ -c CacheBlock.cpp

lru.o: LRUCache.cpp LRUCache.hpp
	g++ -c LRUCache.cpp

clean:
	rm *.o output