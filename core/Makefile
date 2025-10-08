CC := gcc
CFLAGS := -O2 -Iinclude

OBJ := build/obj/version.o

all: lib

build/obj:
	mkdir -p $@
build:
	mkdir -p $@

$(OBJ): src/version.c | build/obj
	$(CC) $(CFLAGS) -c $< -o $@

lib: build $(OBJ)
	ar rcs build/libreports_core.a $(OBJ)

clean:
	rm -rf build
.PHONY: all lib clean

