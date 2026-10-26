
import json
from pathlib import Path


class ScoreManager:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent.parent / "scores.json"
        self.scores = self.load_scores()

    def load_scores(self):
        if not self.file_path.exists():
            return {}

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                return {}

            return data

        except (OSError, json.JSONDecodeError):
            return {}

    def get_high_score(self, game):
        return self.scores.get(game, 0)

    def save_score(self, game, score):
        if score <= self.get_high_score(game):
            return

        self.scores[game] = score

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(self.scores, file, indent=4)

        except OSError as error:
            print(f"Could not save high score: {error}")
