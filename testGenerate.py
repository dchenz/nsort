import argparse
import os
import random
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int)
args = parser.parse_args()
n = args.n

prog = "./main"
if not os.path.exists(prog):
    print("Need to compile the C program...")
    exit(1)


def runCommand(command, input_data):
    result = subprocess.run(
        command, input=input_data, capture_output=True, text=True, shell=True
    )
    return result.stdout


numRange = list(range(-n, n))

for i in range(10000):
    testCase = random.choices(numRange, k=n)
    output = runCommand(prog, " ".join(map(str, testCase)))
    resultNums = list(map(int, output.split(": ")[1].split(" ")))
    assert sorted(testCase) == resultNums, (testCase, resultNums)
