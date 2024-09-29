import argparse
import itertools
from typing import Iterator


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int)
    args = parser.parse_args()
    return args


def getPerms(arg: int) -> Iterator[tuple[tuple[int, ...], tuple[int, ...]]]:
    perms = list(itertools.permutations([v for v in nums if v != arg], n - 1))
    seen = set()
    for p in perms:
        lessThan = tuple(sorted(p[:arg]))
        greaterThan = tuple(sorted(p[arg:]))
        key = (lessThan, greaterThan)
        if key in seen:
            continue
        seen.add(key)
        yield lessThan, greaterThan


def var(v: int) -> str:
    return chr(ord("a") + v)


def processPerms(arg: int) -> str:
    sumExprParts = []
    for i in nums:
        orConditionParts = []
        for lessThan, greaterThan in getPerms(arg):
            andConditionParts = []
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
        dupeGuardParts = []
        for j in range(0, i):
            dupeGuardParts.append(f"{var(i)} != {var(j)}")
        dupeGuard = " && ".join(dupeGuardParts)
        if dupeGuard:
            multiplyCondition = f"{multiplyCondition} * ({dupeGuard})"
        sumExprParts.append(multiplyCondition)
    sumExpr = " + ".join(sumExprParts)
    return sumExpr


def main():
    args = getArgs()

    global n
    global nums
    n = args.n
    nums = list(range(n))

    argExprParts = []
    for arg in nums:
        argExprParts.append("        " + processPerms(arg))
    argExpr = ",\n".join(argExprParts)

    formatExpr = " ".join("%d" for _ in nums)
    varsExpr = ", ".join(f"{var(v)}" for v in nums)
    varsPointersExpr = ", ".join(f"&{var(v)}" for v in nums)

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
