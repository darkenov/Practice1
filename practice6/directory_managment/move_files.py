import os
import shutil

raw = "workspace/project/data/raw"
processed = "workspace/project/data/processed"

os.makedirs(raw, exist_ok=True)
os.makedirs(processed, exist_ok=True)

# create simple test files
open(raw + "/a.txt", "w").write("hello")
open(raw + "/b.txt", "w").write("world")
open(raw + "/c.csv", "w").write("1,2,3")

# 3) Find files by extension (.txt)
for name in os.listdir(raw):
    if name.endswith(".txt"):
        print("Found:", name)

# 4) Copy .txt files raw -> processed
for name in os.listdir(raw):
    if name.endswith(".txt"):
        shutil.copy(raw + "/" + name, processed + "/" + name)

print("Copied .txt files!")

# Move .csv raw -> processed
for name in os.listdir(raw):
    if name.endswith(".csv"):
        shutil.move(raw + "/" + name, processed + "/" + name)

print("Moved .csv files!")