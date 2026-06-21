from src.analytics import Analytics, DailyMetrics
from datetime import date
import pytest

def test_add_daily_metrics():
    analytics = Analytics()
    daily_metrics = DailyMetrics(date=date(2022, 1, 1), signups=10, trial_conversions=5)
    analytics.add_daily_metrics(daily_metrics)
    assert analytics.get_daily_metrics(date(2022, 1, 1)) == daily_metrics

def test_get_daily_metrics():
    analytics = Analytics()
    daily_metrics = DailyMetrics(date=date(2022, 1, 1), signups=10, trial_conversions=5)
    analytics.add_daily_metrics(daily_metrics)
    assert analytics.get_daily_metrics(date(2022, 1, 1)).signups == 10

def test_to_graphql():
    analytics = Analytics()
    daily_metrics1 = DailyMetrics(date=date(2022, 1, 1), signups=10, trial_conversions=5)
    daily_metrics2 = DailyMetrics(date=date(2022, 1, 2), signups=15, trial_conversions=10)
    analytics.add_daily_metrics(daily_metrics1)
    analytics.add_daily_metrics(daily_metrics2)
    result = analytics.to_graphql()
    assert len(result) == 2
    assert result[0]['date'] == '2022-01-01'
    assert result[0]['signups'] == 10
    assert result[1]['date'] == '2022-01-02'
    assert result[1]['signups'] == 15
