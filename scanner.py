from pathlib import Path

from config import PROJECTS_DIR, IMAGE_EXTENSIONS
from database import init_db, add_project, add_image, get_images
from thumbnails import create_thumbnail


def scan_projects():
    init_db()

    if not PROJECTS_DIR.exists():
        print("Projects folder not found")
        return

    print("Scanning projects...")

    for project in PROJECTS_DIR.iterdir():

        if not project.is_dir():
            continue

        project_id = add_project(project.name, str(project))

        existing_images = {img[0] for img in get_images(project_id)}

        for file in project.rglob("*"):

            if not file.is_file():
                continue

            if file.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            file_path = str(file)

            if file_path in existing_images:
                continue

            thumbnail = create_thumbnail(file_path)

            if thumbnail:
                add_image(project_id, file_path, thumbnail)

    print("Scan complete!")

if __name__ == "__main__":
    scan_projects()