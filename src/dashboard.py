import json
from src.analytics import Analytics, DailyMetrics

class Dashboard:
    def __init__(self, analytics):
        self.analytics = analytics

    def display_realtime_charts(self):
        metrics = self.analytics.to_graphql()
        return json.dumps(metrics)
