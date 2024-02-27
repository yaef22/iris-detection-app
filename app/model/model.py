import pickle
import re
from pathlib import Path

__version__ = "1.0.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_SVM_Iris-1.0.0.pkl", "rb") as f:
    model = pickle.load(f)
