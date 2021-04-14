output: main.o ram.o block.o lru.o 
	g++ -c main.o ram.o block.o lru.o -o outputs 

main.o: main.cpp
	g++ -c main.cpp

ram.o: Ram.cpp Ram.hpp
	g++ -c Ram.cpp

block.o: CacheBlock.cpp CacheBlock.hpp
	g++ -c CacheBlock.cpp

lru.o: LRUCache.cpp LRUCache.hpp
	g++ -c LRUCache.cpp

clean:
	rm *.o output