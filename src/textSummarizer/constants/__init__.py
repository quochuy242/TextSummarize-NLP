from pathlib import Path
import os

filepath_project = os.getcwd()
CONFIG_FILE_PATH = Path(filepath_project + "/config/config.yaml")
PARAMS_FILE_PATH = Path(filepath_project + "/params.yaml")

print(CONFIG_FILE_PATH, "\n", PARAMS_FILE_PATH)
