# url_categorizer.py
import csv
import pickle
from pathlib import Path

class URLCategorizer:
    def __init__(self, cat_path="config/categories.csv", model_path="models/url_classifier.pkl"):
        self.static_map = {}
        for row in csv.DictReader(Path(cat_path).open()):
            self.static_map[row["domain"]] = row["category"]

        # Load ML model (XGBoost)
        self.model = pickle.load(open(model_path, "rb"))

    def _extract_features(self, url: str):
        # Very small feature set for demo
        return [len(url), url.count("/"), url.count(".")]

    def categorize(self, url: str):
        # 1) Static lookup
        domain = url.split("//")[-1].split("/")[0].lower()
        if domain in self.static_map:
            return self.static_map[domain], 1.0  # perfect confidence

        # 2) ML prediction
        feat = self._extract_features(url)
        prob = self.model.predict_proba([feat])[0][1]
        category = "Adult" if prob > 0.5 else "Safe"
        return category, prob
