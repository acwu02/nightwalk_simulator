# Feature encapsulates both areas and connectors

import os
import random

PATH = "test"

class Feature():
    def __init__(self, id, dir):
        super().__init__(id)
        self.dir = f"{PATH}/{dir}"
        self.generate_bg()

    def generate_bg(self):
        if os.path.exists(self.path):
            bg_files = [f for f in os.listdir(self.dir) if os.path.isfile(
                os.path.join(self.dir, f))]
            if bg_files:
                self.bg = random.choice(bg_files)
