import os

# 1) Create nested directories
os.makedirs("workspace/project/data/raw", exist_ok=True)
os.makedirs("workspace/project/data/processed", exist_ok=True)
os.makedirs("workspace/project/logs", exist_ok=True)

print("Folders created!")

# 2) List files and folders in workspace/project
items = os.listdir("workspace/project")
print("Items in workspace/project:", items)