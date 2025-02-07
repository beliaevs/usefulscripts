CPP=g++
CPPFLAGS=-std=c++17 -Wall -Wpedantic -Wextra
SOURCES=$(wildcard *.cpp)
EXECUTABLES=$(SOURCES:.cpp=.exe)

all: $(EXECUTABLES)

%.exe: %.cpp
	$(CPP) -o $@ $(CPPFLAGS) $<

