# the compiler: gcc for C program, define as g++ for C++
CC = gcc

# compiler flags:
CFLAGS = -g -Wall -O3

# the build target executable:
TARGET = converter

# typing 'make' will invoke this
default: $(TARGET)

# create executable
$(TARGET):	main.o conversion.o
	$(CC) $(CFLAGS) -o $(TARGET) main.o conversion.o

# make object files
main.o:		main.c conversion.h
	$(CC) $(CFLAGS) -c main.c

conversion.o:	conversion.c conversion.h
	$(CC) $(CFLAGS) -c conversion.c

# to start over from scratch, type 'make clean'.
clean:
	rm -fv $(TARGET) *.o
