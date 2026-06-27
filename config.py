from pathlib import Path

# Root directory containing project folders
PROJECTS_DIR = Path("sample_projects")

# SQLite database
DATABASE = "gallery.db"

# Folder to store thumbnails
THUMBNAILS_DIR = Path("thumbnails")

# Thumbnail size (width, height)
THUMBNAIL_SIZE = (250, 250)

# Supported image extensions
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}