import json
from dataclasses import dataclass
from datetime import date

@dataclass
class DailyMetrics:
    date: date
    signups: int
    trial_conversions: int

class Analytics:
    def __init__(self):
        self.metrics = {}

    def add_daily_metrics(self, daily_metrics):
        self.metrics[daily_metrics.date] = daily_metrics

    def get_daily_metrics(self, date):
        return self.metrics.get(date)

    def to_graphql(self):
        result = []
        for daily_metrics in self.metrics.values():
            result.append({
                'date': daily_metrics.date.isoformat(),
                'signups': daily_metrics.signups,
                'trial_conversions': daily_metrics.trial_conversions
            })
        return result
