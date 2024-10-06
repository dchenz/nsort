N ?= 3

all: generate build test

generate:
	python3 generate.py -n ${N} > main.c

build:
	gcc -Wall -Werror -o main main.c

test:
	python3 testGenerate.py -n ${N}
