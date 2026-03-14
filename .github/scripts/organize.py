import os
import shutil
import json

topics = {
    "array": "01-arrays",
    "remove": "01-arrays",
    "rotate": "01-arrays",
    "matrix": "01-arrays",
    "two": "02-two-pointers",
    "sum": "02-two-pointers",
    "zigzag": "03-sliding-window",
    "stack": "04-stack",
    "parentheses": "04-stack",
    "search": "05-binary-search",
    "list": "06-linked-list",
    "tree": "07-trees",
    "heap": "08-heap",
    "graph": "09-graphs",
    "sudoku": "09-graphs",
    "dfs": "09-graphs",
    "bfs": "09-graphs",
    "dp": "10-dynamic-programming",
    "dynamic": "10-dynamic-programming",
    "backtrack": "11-backtracking",
    "combination": "11-backtracking",
    "permutation": "11-backtracking",
    "greedy": "12-greedy",
    "bit": "14-bit-manipulation",
    "string": "15-strings",
    "prefix": "15-strings",
    "anagram": "15-strings",
    "hash": "17-hash-table",
    "set": "17-hash-table",
    "prefix": "18-prefix-sum",
    "sum": "18-prefix-sum",
    "interval": "19-intervals",
    "sort": "20-sorting",
    "union": "21-union-find",
    "queue": "23-queue", 
    "trie": "22-trie",

    # math related keywords
    "math": "13-math",
    "integer": "13-math",
    "number": "13-math",
    "roman": "13-math",
    "pow": "13-math",
    "sqrt": "13-math",
    "divide": "13-math",
    "multiply": "13-math",
    "plus": "13-math",
}

IGNORE = {
    ".git",
    ".github",
    "organize.py",
    "update_readme.py",
    "fetch_leetcode.py",
    "README.md",
    "problems.json"
}

topics_folders = set(topics.values())
topics_folders.add("16-misc")

metadata_file = "problems.json"

if os.path.exists(metadata_file):
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)
else:
    metadata = {}

items = os.listdir(".")

for item in items:

    if item in IGNORE:
        continue

    if item in topics_folders:
        continue

    if item.startswith("."):
        continue

    if not os.path.isdir(item):
        continue

    lower = item.lower()
    moved = False

    for key in topics:

        if key in lower:

            folder = topics[key]
            os.makedirs(folder, exist_ok=True)

            dest = os.path.join(folder, item)

            if not os.path.exists(dest):
                shutil.move(item, dest)

            moved = True
            break

    if not moved:

        os.makedirs("16-misc", exist_ok=True)

        dest = os.path.join("16-misc", item)

        if not os.path.exists(dest):
            shutil.move(item, dest)

    metadata[item] = {
        "name": item
    }

with open(metadata_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
