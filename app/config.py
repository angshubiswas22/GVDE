import os

from dotenv import load_dotenv

load_dotenv()


# =====================================================
# Project Information
# =====================================================

PROJECT_NAME = "GeoVision Dataset Engine"
PROJECT_SHORT_NAME = "GVDE"
VERSION = "0.1.0"


# =====================================================
# Database Configuration
# =====================================================

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# =====================================================
# Dataset Defaults
# =====================================================

DEFAULT_HEADINGS = [
    0,
    60,
    120,
    180,
    240,
    300
]

DEFAULT_SAMPLE_DISTANCE = 50

DEFAULT_FOV = 90


# =====================================================
# Storage
# =====================================================

IMAGE_ROOT = "data/images"
METADATA_ROOT = "data/metadata"