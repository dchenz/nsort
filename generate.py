import argparse
import itertools
import os
from concurrent.futures import Future, ProcessPoolExecutor
from typing import Iterator


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int)
    args = parser.parse_args()
    return args


def getPerms(n: int, arg: int) -> Iterator[tuple[tuple[int, ...], tuple[int, ...]]]:
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for p in itertools.permutations([v for v in range(n) if v != arg], n - 1):
        lessThan = tuple(sorted(p[:arg]))
        greaterThan = tuple(sorted(p[arg:]))
        key = (lessThan, greaterThan)
        if key in seen:
            continue
        seen.add(key)
        yield lessThan, greaterThan


def var(v: int) -> str:
    return chr(ord("a") + v)


def getMultiplyCondition(n: int, arg: int, i: int) -> str:
    orConditionParts: list[str] = []
    for lessThan, greaterThan in getPerms(n, arg):
        andConditionParts: list[str] = []
        for v in lessThan:
            v += i - arg
            v %= n
            andConditionParts.append(f"{var(v)} <= {var(i)}")
        for v in greaterThan:
            v += i - arg
            v %= n
            andConditionParts.append(f"{var(i)} <= {var(v)}")
        if andConditionParts:
            andCondition = " && ".join(andConditionParts)
            orConditionParts.append(andCondition)
    if len(orConditionParts) > 1:
        orConditionParts = [f"({part})" for part in orConditionParts]
    if orConditionParts:
        orCondition = f"({' || '.join(orConditionParts)})"
        multiplyCondition = f"{orCondition} * {var(i)}"
    else:
        multiplyCondition = var(i)
    dupeGuardParts: list[str] = []
    for j in range(0, i):
        dupeGuardParts.append(f"{var(i)} != {var(j)}")
    dupeGuard = " && ".join(dupeGuardParts)
    if dupeGuard:
        multiplyCondition = f"{multiplyCondition} * ({dupeGuard})"
    return multiplyCondition


def getArgExpression(n: int) -> Iterator[str]:
    cpuCount = os.cpu_count() or 1
    with ProcessPoolExecutor(max_workers=max(1, cpuCount - 2)) as executor:
        sumExprParts: list[Future[str]] = []
        for arg in range(n):
            for i in range(n):
                sumExprParts.append(executor.submit(getMultiplyCondition, n, arg, i))
        for i in range(n):
            yield "        " + " + ".join(
                sumExpr.result() for sumExpr in sumExprParts[i * n : (i + 1) * n]
            )


def main():
    args = getArgs()

    n = args.n

    formatExpr = " ".join("%d" for _ in range(n))
    varsExpr = ", ".join(f"{var(v)}" for v in range(n))
    varsPointersExpr = ", ".join(f"&{var(v)}" for v in range(n))
    argExpr = ",\n".join(getArgExpression(n))

    prog = f"""#include <stdio.h>

int main() {{
    int {varsExpr};
    printf("Enter {n} numbers separated by space: ");
    scanf("{formatExpr}", {varsPointersExpr});
    printf("{formatExpr}\\n",
{argExpr}
    );
    return 0;
}}"""

    print(prog)


if __name__ == "__main__":
    main()
