exec : \
 compile
    echo "Executing the object file"
    ./compile

compile : main.o hello.o factorial.o
    echo "Compiling"
    gcc -o compile $^

main.o : main.c functions.h
    gcc -c main.c -I./INCLUDE -I./SRC

hello.o : hello.c functions.h
    gcc -c hello.c -I./INCLUDE -I./SRC

factorial.o : factorial.c functions.h
    gcc -c factorial.c -I./INCLUDE -I./SRC