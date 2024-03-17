from pathlib import Path
import os

PROJECT_PATH = Path(os.getcwd())
CONFIG_FILE_PATH = Path(f"{PROJECT_PATH}/config/config.yaml")
PARAMS_FILE_PATH = Path(f"{PROJECT_PATH}/params.yaml")

print(CONFIG_FILE_PATH, "\n", PARAMS_FILE_PATH)
