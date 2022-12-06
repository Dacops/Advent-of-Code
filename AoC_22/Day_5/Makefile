CFLAGS = -O3 -std=c++11 -Wall

day5: day5-1.cpp day5-2.cpp
	g++ $(CFLAGS) day5-1.cpp -o day5-1
	g++ $(CFLAGS) day5-2.cpp -o day5-2

run1: day5-1
	./day5-1 < input.txt
run2: day5-2
	./day5-2 < input.txt
clean:
	rm -f day5-1 day5-2


