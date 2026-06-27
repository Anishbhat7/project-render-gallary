# 📁 Project Render Gallery (Python + Streamlit)

A lightweight internal tool for browsing, searching, and managing architectural project render images stored in local folders.

The app automatically scans project directories, generates thumbnails, stores metadata in SQLite, and provides a clean web-based gallery using Streamlit.

---

## 🚀 Features

- 📂 Recursive scanning of project folders
- 🖼️ Automatic thumbnail generation using Pillow
- 🗄️ SQLite database for structured storage
- 🔍 Search projects by name
- 🖥️ Streamlit-based web gallery UI
- 🧹 Clear database reset option
- 📊 Image count per project
- ⚡ Fast local browsing of large image datasets

---

## 🧱 Project Structure


StreamLitApp/

├── app.py # Streamlit UI

├── scanner.py # Folder scanning logic

├── database.py # SQLite database layer

├── thumbnails.py # Thumbnail generation

├── config.py # Configuration settings

├── gen_test_images.py # Generates sample images for testing

├── requirements.txt # Dependencies

├── sample_projects/ # Example project folders

└── thumbnails/ # Generated thumbnails


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/project-render-gallery.git
cd project-render-gallery
2. Install dependencies
pip install -r requirements.txt
3. (Optional) Generate sample data
python gen_test_images.py

This will create sample project folders with fake render images.

4. Run the application
streamlit run app.py
🧠 How It Works
1. Scan Projects

The app recursively scans the sample_projects/ directory and detects image files inside each project folder.

2. Thumbnail Generation

Images are processed using Pillow to generate lightweight thumbnails for faster UI rendering.

3. Database Storage

All project and image metadata is stored in a local SQLite database for quick querying.

4. Web Interface

Streamlit provides a simple gallery UI where users can:

Browse projects
View thumbnails in grid layout
Search projects
Open images in full-screen mode
🗃️ Database Schema
Projects Table
id | name | path
Images Table
id | project_id | image_path | thumbnail_path
🧹 Utility Features
Clear Database

The “Clear Database” button resets the system by:

Removing all projects
Removing all image records
Allowing a fresh re-scan of folders
📦 Requirements
streamlit
Pillow
🎯 Purpose

This tool is designed for internal use in companies that manage large collections of project renderings.

It helps to:

Quickly browse past design projects
Reuse existing design work
Replace manual folder navigation with a visual system
Centralize image indexing into a searchable interface


🔮 Future Improvements
Incremental scanning (only new/changed files)
Authentication system for internal access
Advanced filtering (tags, categories)
Pinterest-style masonry UI
Cloud deployment (Streamlit Cloud / Docker)