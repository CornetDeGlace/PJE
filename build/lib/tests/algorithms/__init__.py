# tests/algorithms/__init__.py

import os
import sys

# Get the current directory of this file
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# Get the project path (one level up from the current directory)
PROJECT_PATH = os.path.abspath(os.path.join(CURRENT_DIR, '..'))

# Get the source path and algorithms path
SOURCE_PATH = os.path.join(PROJECT_PATH, 'src')
ALGO_PATH = os.path.join(SOURCE_PATH, 'algorithms')

# Add the source and algorithms path to sys.path
sys.path.append(SOURCE_PATH)
sys.path.append(ALGO_PATH)