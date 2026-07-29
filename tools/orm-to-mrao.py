## Source 2 uses ORM (or atleast Source 2 Viewer exports them as it), While strata uses MRAO.
## ImageMagick allows for images to be turned in the right format easily, and quickly.
## Just drag and drop image files onto this

from pathlib import Path
import subprocess
import os
import sys

IMAGE_EXTS = {
    ".png", ".jpg", ".jpeg", ".tga",
    ".bmp", ".tif", ".tiff", ".dds", ".webp"
}

def process_file(file):
    temp = file.with_name(file.stem + "_temp" + file.suffix)

    subprocess.run([
        "magick",
        str(file),
        "-channel", "RGB",
        "-separate",
        "(",
        "+clone",
        ")",
        "-swap", "0,2",
        "-delete", "3",
        "-combine",
        str(temp)
    ], check=True)

    os.replace(temp, file)
    print(f"Converted: {file}")

if len(sys.argv) < 2:
    print("Drag files or folders onto this script.")
    input("Press Enter to exit...")
    sys.exit()

for arg in sys.argv[1:]:
    path = Path(arg)

    if path.is_file():
        if path.suffix.lower() in IMAGE_EXTS:
            process_file(path)

    elif path.is_dir():
        for file in path.rglob("*"):
            if file.suffix.lower() in IMAGE_EXTS:
                process_file(file)

print("Done!")
input("Press Enter to exit...")