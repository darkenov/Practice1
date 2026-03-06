from pathlib import Path

def main():
    base = Path(__file__).parent
    work = base / "workspace"

    # 1) Create nested directories
    (work / "project" / "data" / "raw").mkdir(parents=True, exist_ok=True)
    (work / "project" / "data" / "processed").mkdir(parents=True, exist_ok=True)
    (work / "project" / "logs").mkdir(parents=True, exist_ok=True)

    print("Directories created inside:", work)

    # Create a couple of test files (so listing shows something)
    raw = work / "project" / "data" / "raw"
    (raw / "a.txt").write_text("hello\n", encoding="utf-8")
    (raw / "b.csv").write_text("1,2,3\n", encoding="utf-8")

    # 2) List files and folders in project directory
    project = work / "project"
    folders = [p.name for p in project.iterdir() if p.is_dir()]
    files = [p.name for p in project.iterdir() if p.is_file()]

    print("\nInside 'project':")
    print("Folders:", folders)
    print("Files:", files)

    # List content inside raw folder
    print("\nInside 'raw':")
    for p in raw.iterdir():
        print("-", p.name)

if __name__ == "__main__":
    main()