all: driver

driver: driver.o
	g++ -o driver driver.o -lwiringPi  

driver.o: driver.cpp
	g++ -c driver.cpp

clean:
	rm -rf *.o driver
