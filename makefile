SRCS = $(wildcard *.cpp)
HDRS = $(wildcard *h) $(wildcard *.hpp)
PROJ = graphs

CC = g++      
APP = $(PROJ).so 
CFLAGS = --std=c++0x -fPIC -shared 
LDFLAGS = -ldl
LIBS =
all: $(APP)      

$(APP): $(OBJS)
	$(CC) $(CFLAGS) $(SRCS) -o $(APP) $(LIBS)   


.PHONY:clean
clean:     
	rm -f *.o *~ $(APP)  

.PHONY:gdb
gdb:
	gdb ./$(APP)
