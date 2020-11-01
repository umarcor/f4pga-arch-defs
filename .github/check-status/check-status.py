#!/usr/bin/env python3

from pathlib import Path
from json import load

data = load(Path('event.json').open('r'))

print(data)

for item in data:
    print("·", item)
    print(data[item])
    print()
