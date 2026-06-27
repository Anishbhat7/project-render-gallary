from PIL import Image, ImageDraw
from pathlib import Path
import random

base = Path("sample_projects")

projects = [
    "Stair Project",
    "Modern Railings",
    "Spiral Stair"
]

# Ensure folders exist
for p in projects:
    (base / p).mkdir(parents=True, exist_ok=True)


def make_realistic_image(path, title):
    width, height = 900, 600

    # random dark background (more "render-like")
    bg = (
        random.randint(20, 60),
        random.randint(20, 60),
        random.randint(20, 60)
    )

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)

    # draw fake "structure lines" (like railings/stairs)
    for i in range(8):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        color = (
            random.randint(120, 255),
            random.randint(120, 255),
            random.randint(120, 255)
        )

        draw.line((x1, y1, x2, y2), fill=color, width=3)

    # add fake project text
    text = f"{title}"
    draw.text((30, 30), text, fill=(255, 255, 255))

    # save
    img.save(path)


# Generate images
for project in base.iterdir():
    if project.is_dir():
        for i in range(5):
            make_realistic_image(project / f"render_{i+1}.jpg", project.name)

print("Realistic test images created")