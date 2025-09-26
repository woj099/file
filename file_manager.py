import os
import csv
import json
import time


class File:
    def __init__(self, root_folder):
        self.root_folder = root_folder
        os.makedirs("info", exist_ok=True)
        self.info_folder = "info"
        try:
            os.makedirs(self.root_folder, exist_ok=True)
        except:
            print(f"root folder '{self.root_folder}' created")
        self.index = os.path.join(self.info_folder, f"{os.path.basename(folder)}.csv")
        if os.path.exists(self.index):
            with open(self.index, "r") as f:
                content = f.read().strip()