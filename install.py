from pathlib import Path
import os
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while process.stdout.readable():
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode().strip())

print("Installing environment ...")
run_command("conda env create --name tutorial_diss --file env.yaml")
print("Install pre-commit ...")
run_command("conda run --name tutorial_diss pre-commit install")
print("Updating pre-commit hooks ...")
run_command("conda run --name tutorial_diss pre-commit autoupdate")
