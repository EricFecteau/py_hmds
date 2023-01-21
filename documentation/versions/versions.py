"""Get the information of the rom files"""

from pathlib import Path
import hashlib

path_root = Path("./roms")

# For main paths (hmds vs hmds-cute)
for path in path_root.iterdir():
    if not path_root.is_dir():
        continue

    print(f"--------{path}--------")

    # For sub paths (region)
    for sub_path in path.iterdir():
        if not sub_path.is_dir():
            continue

        print(f"\t{sub_path}")

        # For rom
        for file in sub_path.glob("**/*.nds"):
            print(f"\t\t{file}")
            with file.open("rb") as f:
                version = f.read(0x1F)[-1]
                print(f"\t\t\tVersion: {version}")
            print(f"\t\t\tSha256: {hashlib.sha256(file.read_bytes()).hexdigest()}")
