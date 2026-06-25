import pytest
from ai_tutor import generate_progress_report, send_progress_report, cron_job
from datetime import datetime, timedelta

def test_generate_progress_report():
    learner_data = {
        'modules': [
            {'name': 'Module 1', 'completed': True, 'hint_rating': 4},
            {'name': 'Module 2', 'completed': False, 'hint_rating': 3},
            {'name': 'Module 3', 'completed': True, 'hint_rating': 5}
        ]
    }
    report = generate_progress_report(learner_data)
    assert len(report.completed_modules) == 2
    assert report.average_hint_rating == (4 + 5) / 2
    assert report.recommended_next_topics == ['Module 2']

def test_send_progress_report():
    report = generate_progress_report({
        'modules': [
            {'name': 'Module 1', 'completed': True, 'hint_rating': 4},
            {'name': 'Module 2', 'completed': False, 'hint_rating': 3},
            {'name': 'Module 3', 'completed': True, 'hint_rating': 5}
        ]
    })
    send_progress_report(report, 'test@example.com')

def test_cron_job():
    learner_data = {
        'modules': [
            {'name': 'Module 1', 'completed': True, 'hint_rating': 4},
            {'name': 'Module 2', 'completed': False, 'hint_rating': 3},
            {'name': 'Module 3', 'completed': True, 'hint_rating': 5}
        ]
    }
    cron_job(learner_data, 'test@example.com')

def test_generate_progress_report_empty():
    learner_data = {
        'modules': []
    }
    report = generate_progress_report(learner_data)
    assert len(report.completed_modules) == 0
    assert report.average_hint_rating == 0
    assert report.recommended_next_topics == []

def test_send_progress_report_empty():
    report = generate_progress_report({
        'modules': []
    })
    send_progress_report(report, 'test@example.com')
