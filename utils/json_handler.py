import json
import os
from utils.logger import logger

class JSONHandler:
    @staticmethod
    def load_json(filepath):
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception:
            return []

    @staticmethod
    def save_json(filepath, data):
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Failed to save file: {e}")
            return False