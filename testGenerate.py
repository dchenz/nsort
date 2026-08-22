import argparse
import random
import subprocess


def getArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int)
    args = parser.parse_args()
    return args


def runTest(testCase: list[int]):
    actualResult = list(
        map(
            int,
            subprocess.run(
                "./main",
                input=" ".join(map(str, testCase)),
                capture_output=True,
                text=True,
                shell=True,
            )
            .stdout.split(": ")[1]
            .split(" "),
        )
    )
    assert (
        sorted(testCase) == actualResult
    ), f"Incorrect sort: {testCase} -> {actualResult}"


def main():
    args = getArgs()

    random.seed(1)

    for _ in range(100):
        testCase = random.choices(range(-args.n // 2, args.n // 2), k=args.n)
        runTest(testCase)


if __name__ == "__main__":
    main()
