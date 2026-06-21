import json
from dataclasses import dataclass
from typing import List

@dataclass
class Lab:
    id: int
    code: str
    test_cases: List[str]

@dataclass
class AIHint:
    suggestion: str

class CurriculumEngine:
    def __init__(self):
        self.labs = []
        self.ai_hints = {}

    def add_lab(self, lab: Lab):
        self.labs.append(lab)
        self.ai_hints[lab.id] = []

    def add_ai_hint(self, lab_id: int, hint: AIHint):
        if lab_id in self.ai_hints:
            self.ai_hints[lab_id].append(hint.suggestion)

    def get_ai_hints(self, lab_id: int) -> List[str]:
        return self.ai_hints.get(lab_id, [])

    def run_lab(self, lab_id: int, code: str) -> bool:
        lab = next((lab for lab in self.labs if lab.id == lab_id), None)
        if lab:
            # Run test cases
            for test_case in lab.test_cases:
                try:
                    exec(test_case)
                except Exception:
                    return False
            return True
        return False

    def record_completion(self, lab_id: int) -> bool:
        lab = next((lab for lab in self.labs if lab.id == lab_id), None)
        if lab:
            # Check if lab is completed
            if self.run_lab(lab_id, lab.code):
                return True
        return False
