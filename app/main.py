import os
import sys

version = "3.12"

print(f"Hello world from Python {version}")

print()

print(f"Current working directory: {os.getcwd()}")
print(f"Files in the current directory: {os.listdir('.')}")

print()

for i in range(5):
    print(f"Magic number {i}: {os.urandom(8)}")

print()

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")