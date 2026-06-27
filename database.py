import sqlite3
from config import DATABASE


def get_connection():
    return sqlite3.connect(DATABASE)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        path TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        image_path TEXT UNIQUE,
        thumbnail_path TEXT,
        FOREIGN KEY(project_id) REFERENCES projects(id)
    )
    """)

    conn.commit()
    conn.close()


def add_project(name, path):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO projects(name, path) VALUES (?, ?)",
        (name, path)
    )

    conn.commit()

    cursor.execute(
        "SELECT id FROM projects WHERE name = ?",
        (name,)
    )

    project_id = cursor.fetchone()[0]
    conn.close()
    return project_id


def add_image(project_id, image_path, thumbnail_path):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO images(project_id, image_path, thumbnail_path)
        VALUES (?, ?, ?)
    """, (project_id, image_path, thumbnail_path))

    conn.commit()
    conn.close()


def get_projects(search=""):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name
        FROM projects
        WHERE name LIKE ?
        ORDER BY name
    """, (f"%{search}%",))

    projects = cursor.fetchall()
    conn.close()
    return projects


def get_images(project_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT image_path, thumbnail_path
        FROM images
        WHERE project_id = ?
    """, (project_id,))

    images = cursor.fetchall()
    conn.close()
    return images

def clear_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM images")
    cursor.execute("DELETE FROM projects")

    conn.commit()
    conn.close()