# nsort

This script generates a C program that reads N integers from stdin and prints them in sorted order.

It uses at most N variables, contains no conditional statements, and includes only one `printf`.

## Usage

```sh
# Creates a file named "main.c". Larger N take longer to run.
make generate N=8

# Compiles the C program.
make build

# Runs tests against the compiled binary.
make test N=8

# Runs all of the above.
make N=8
```

## Examples

```
./main
Enter 8 numbers separated by space: 24 12 3 0 -11 -20 4 1
-20 -11 0 1 3 4 12 24

./main
Enter 8 numbers separated by space: 24 -1 1 0 -2 -2 -2 8
-2 -2 -2 -1 0 1 8 24
```
