import os
import streamlit as st
from PIL import Image

from scanner import scan_projects
from database import init_db, get_projects, get_images, clear_database


st.set_page_config(
    page_title="Project Gallery",
    layout="wide"
)

st.title("📁 Project Render Gallery")

# Initialize database
init_db()

# Sidebar
with st.sidebar:
    st.header("Actions")

    if st.button("🔄 Scan Projects"):
        with st.spinner("Scanning projects..."):
            scan_projects()
        st.success("Scan completed!")

    st.divider()

    if st.button("🗑️ Clear Database"):
        clear_database()
        st.success("Database cleared!")
        st.rerun()

# Search
search = st.text_input("🔍 Search Project")

projects = get_projects(search)

if not projects:
    st.info("No projects found. Click 'Scan Projects' to index your folders.")
    st.stop()


# Display projects
for project_id, project_name in projects:

    images = get_images(project_id)
    image_count = len(images)

    st.subheader(f"{project_name} ({image_count} images)")

    images = get_images(project_id)

    if not images:
        st.write("No images found.")
        continue

    cols = st.columns(4)

    for i, (image_path, thumbnail_path) in enumerate(images):

        col = cols[i % 4]

        if os.path.exists(thumbnail_path):
            with col:
                st.image(
                    thumbnail_path,
                    use_container_width=True
                )