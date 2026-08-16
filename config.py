import os

# ==========================================
# Application
# ==========================================
APP_NAME = "Student Management System ERP"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

THEME = "blue"
MODE = "light"

# ==========================================
# Fonts
# ==========================================

TITLE_FONT = ("Arial", 26, "bold")
HEADING_FONT = ("Arial", 18, "bold")
TEXT_FONT = ("Arial", 14)

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_FOLDER = os.path.join(BASE_DIR, "database")
ASSETS_FOLDER = os.path.join(BASE_DIR, "assets")
EXPORT_FOLDER = os.path.join(BASE_DIR, "exports")

DATABASE_PATH = os.path.join(DATABASE_FOLDER, "erp.db")

# Folder automatically create
os.makedirs(DATABASE_FOLDER, exist_ok=True)
os.makedirs(ASSETS_FOLDER, exist_ok=True)
os.makedirs(EXPORT_FOLDER, exist_ok=True)