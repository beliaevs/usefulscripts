CPP=g++
CPPFLAGS=-std=c++17 -Wall -Wpedantic -Wextra

all: $(patsubst %.cpp, %.exe, $(wildcard *.cpp))

%.exe: %.cpp
	$(CPP) -o $@ $(CPPFLAGS) $<

