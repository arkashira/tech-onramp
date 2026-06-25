import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Module:
    name: str
    completed: bool
    hint_rating: int

@dataclass
class ProgressReport:
    completed_modules: List[Module]
    average_hint_rating: float
    recommended_next_topics: List[str]

def generate_progress_report(learner_data: dict) -> ProgressReport:
    completed_modules = []
    total_hint_rating = 0
    for module in learner_data['modules']:
        if module['completed']:
            completed_modules.append(Module(module['name'], module['completed'], module['hint_rating']))
            total_hint_rating += module['hint_rating']
    average_hint_rating = total_hint_rating / len(completed_modules) if completed_modules else 0
    recommended_next_topics = [module['name'] for module in learner_data['modules'] if not module['completed']]
    return ProgressReport(completed_modules, average_hint_rating, recommended_next_topics)

def send_progress_report(report: ProgressReport, email: str) -> None:
    # Simulate sending an email
    print(f"Sending progress report to {email}")
    print(json.dumps(report.__dict__, default=lambda x: x.__dict__, indent=4))

def cron_job(learner_data: dict, email: str) -> None:
    report = generate_progress_report(learner_data)
    send_progress_report(report, email)
