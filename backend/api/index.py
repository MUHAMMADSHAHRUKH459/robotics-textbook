from fastapi import FastAPI
from mangum import Mangum
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app

# Wrap FastAPI with Mangum for serverless
handler = Mangum(app)