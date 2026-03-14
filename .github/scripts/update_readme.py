import os
import json

topics = [
"01-arrays",
"02-two-pointers",
"03-sliding-window",
"04-stack",
"05-binary-search",
"06-linked-list",
"07-trees",
"08-heap",
"09-graphs",
"10-dynamic-programming",
"11-backtracking",
"12-greedy",
"13-math",
"14-bit-manipulation",
"15-strings",
"16-misc"
]

metadata_file = "problems.json"

if os.path.exists(metadata_file):
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)
else:
    metadata = {}

rows = ""
problem_rows = ""
total = 0

for topic in topics:

    if os.path.exists(topic):

        files = [
            f for f in os.listdir(topic)
            if os.path.isdir(os.path.join(topic, f))
        ]

        count = len(files)
        total += count

        rows += f"| {topic} | {count} |\n"

        for file in files:

            number = file.split("-")[0]

            name = file.replace(".py","").replace(".cpp","").replace(".java","")

            title = name.split("-",1)[1].replace("-", " ").title()

            url_name = title.lower().replace(" ", "-")

            link = f"https://leetcode.com/problems/{url_name}/"

            problem_rows += f"| {number} | [{title}]({link}) | {topic} |\n"


readme = f"""# 🚀 LeetCode Problem Archive

Automatically synced solutions from LeetCode.

## 📊 Statistics

**Total Problems Solved: {total}**

| Topic | Problems |
|------|------|
{rows}

---

## 📚 Problems

| # | Problem | Topic |
|---|---|---|
{problem_rows}

---

## 📂 Repository Structure

Problems are organized by **DSA topics**.

---

## ⚙️ Automation

This repository automatically:

• syncs solved problems from LeetCode  
• organizes them by topic  
• updates README statistics  

using GitHub Actions.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
