import sys
from pathlib import Path

backend_directory = Path(__file__).resolve().parent / "backend"
sys.path.insert(0, str(backend_directory))

from backend.main import app
