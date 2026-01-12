from pathlib import Path

# ==================================================
# Project paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parent

APP_DIR = BASE_DIR / "app"
DOMAIN_DIR = BASE_DIR / "domain"
PERSISTENCE_DIR = BASE_DIR / "persistence"

DATA_DIR = BASE_DIR / "data"
IMAGES_DIR = BASE_DIR / "images"


# ==================================================
# UI configuration
# ==================================================

WINDOW_TITLE = "Flashy"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 613
WINDOW_PADDING = 50

BACKGROUND_COLOR = "#B1DDC6"


# ==================================================
# Image files
# ==================================================

CARD_FRONT_IMAGE = IMAGES_DIR / "card_front.png"
CARD_BACK_IMAGE = IMAGES_DIR / "card_back.png"

BUTTON_OK_IMAGE = IMAGES_DIR / "right.png"
BUTTON_NOK_IMAGE = IMAGES_DIR / "wrong.png"


# ==================================================
# Data / training
# ==================================================

PREFIX = "training_"
CSV_ENCODING = "utf-8"