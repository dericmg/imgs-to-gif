from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--tempo", type=int, default=100)
args = parser.parse_args()

images = []
for img in sorted(os.listdir(), key=lambda x: (int(x.split('.')[0]) if x.split('.')[0].isdigit() else float('inf'))):
    if img.lower().endswith(('.jpeg', '.jpg', '.png')):
        images.append(Image.open(img).convert("RGBA"))

if images:
    images[0].save(
        "output.gif",
        save_all=True,
        append_images=images[1:],
        duration=args.tempo,
        loop=0,
        disposal=2
    )
