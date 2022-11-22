import os


DATA_DIR = "./data/"
SNAPSHOTS_DIR = "./snapshots/"
MOVIES_DIR = "./movies/"
LOG_DIR = "./logs/"


folders = [DATA_DIR, SNAPSHOTS_DIR, MOVIES_DIR, LOG_DIR]
for folder in folders:
    try:
        os.mkdir(folder)
    except FileExistsError:
    	pass
