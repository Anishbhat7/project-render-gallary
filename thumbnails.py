from pathlib import Path
from PIL import Image

from config import THUMBNAILS_DIR, THUMBNAIL_SIZE

THUMBNAILS_DIR.mkdir(parents=True, exist_ok=True)


def create_thumbnail(image_path):

    image_path = Path(image_path)

    thumbnail_path = THUMBNAILS_DIR / f"{image_path.stem}.jpg"

    if thumbnail_path.exists():
        return str(thumbnail_path)

    try:
        with Image.open(image_path) as img:
            img.thumbnail(THUMBNAIL_SIZE)
            img.convert("RGB").save(thumbnail_path, "JPEG")
    except Exception as e:
        print(f"Thumbnail error: {e}")
        return None

    return str(thumbnail_path)