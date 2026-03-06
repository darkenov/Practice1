from pathlib import Path
import shutil

def main():
    base = Path(__file__).parent
    work = base / "workspace"
    raw = work / "project" / "data" / "raw"
    processed = work / "project" / "data" / "processed"

    raw.mkdir(parents=True, exist_ok=True)
    processed.mkdir(parents=True, exist_ok=True)

    # Create test files (safe: only inside workspace/)
    (raw / "one.txt").write_text("one\n", encoding="utf-8")
    (raw / "two.txt").write_text("two\n", encoding="utf-8")
    (raw / "three.csv").write_text("1,2,3\n", encoding="utf-8")

    # 3) Find files by extension (example: .txt)
    ext = ".txt"
    found = list(raw.glob(f"*{ext}"))

    print(f"Found {len(found)} '{ext}' files in raw:")
    for f in found:
        print("-", f.name)

    # 4) Copy files from raw -> processed
    print("\nCopying .txt files from raw -> processed")
    for f in found:
        shutil.copy2(f, processed / f.name)

    print("Now in processed:")
    print([p.name for p in processed.iterdir()])

    # 4) Move files (example: move .csv)
    print("\nMoving .csv files from raw -> processed")
    for f in raw.glob("*.csv"):
        shutil.move(str(f), str(processed / f.name))

    print("\nAfter moving:")
    print("raw:", [p.name for p in raw.iterdir()])
    print("processed:", [p.name for p in processed.iterdir()])

if __name__ == "__main__":
    main()