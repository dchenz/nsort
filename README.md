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

```c
#include <stdio.h>

int main() {
    int a, b, c, d;
    printf("Enter 4 numbers separated by space: ");
    scanf("%d %d %d %d", &a, &b, &c, &d);
    printf("%d %d %d %d\n",
        (a <= b && a <= c && a <= d) * a + (b <= c && b <= d && b <= a) * b * (b != a) + (c <= d && c <= a && c <= b) * c * (c != a && c != b) + (d <= a && d <= b && d <= c) * d * (d != a && d != b && d != c),
        ((d <= a && a <= b && a <= c) || (b <= a && a <= d && a <= c) || (c <= a && a <= d && a <= b)) * a + ((a <= b && b <= c && b <= d) || (c <= b && b <= a && b <= d) || (d <= b && b <= a && b <= c)) * b * (b != a) + ((b <= c && c <= d && c <= a) || (d <= c && c <= b && c <= a) || (a <= c && c <= b && c <= d)) * c * (c != a && c != b) + ((c <= d && d <= a && d <= b) || (a <= d && d <= c && d <= b) || (b <= d && d <= c && d <= a)) * d * (d != a && d != b && d != c),
        ((c <= a && d <= a && a <= b) || (c <= a && b <= a && a <= d) || (d <= a && b <= a && a <= c)) * a + ((d <= b && a <= b && b <= c) || (d <= b && c <= b && b <= a) || (a <= b && c <= b && b <= d)) * b * (b != a) + ((a <= c && b <= c && c <= d) || (a <= c && d <= c && c <= b) || (b <= c && d <= c && c <= a)) * c * (c != a && c != b) + ((b <= d && c <= d && d <= a) || (b <= d && a <= d && d <= c) || (c <= d && a <= d && d <= b)) * d * (d != a && d != b && d != c),
        (b <= a && c <= a && d <= a) * a + (c <= b && d <= b && a <= b) * b * (b != a) + (d <= c && a <= c && b <= c) * c * (c != a && c != b) + (a <= d && b <= d && c <= d) * d * (d != a && d != b && d != c)
    );
    return 0;
}
```
