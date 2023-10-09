import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
ALGO_PATH = os.path.join(
    SOURCE_PATH,"algorithms"
)

sys.path.append(SOURCE_PATH)
sys.path.append(ALGO_PATH)

