from src.dashboard import Dashboard
from src.analytics import Analytics, DailyMetrics
from datetime import date
import pytest
import json

def test_display_realtime_charts():
    analytics = Analytics()
    daily_metrics = DailyMetrics(date=date(2022, 1, 1), signups=10, trial_conversions=5)
    analytics.add_daily_metrics(daily_metrics)
    dashboard = Dashboard(analytics)
    result = dashboard.display_realtime_charts()
    assert json.loads(result) == [{'date': '2022-01-01', 'signups': 10, 'trial_conversions': 5}]
