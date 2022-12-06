CFLAGS = -O3 -std=c++11 -Wall

day5: day6-1.cpp day6-2.cpp
	g++ $(CFLAGS) day6-1.cpp -o day6-1
	g++ $(CFLAGS) day6-2.cpp -o day6-2

run1: day6-1
	./day6-1 < input.txt
run2: day6-2
	./day6-2 < input.txt
clean:
	rm -f day6-1 day6-2


